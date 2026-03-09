import logging
import math
import pickle
import time
import warnings
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from tqdm import tqdm

warnings.filterwarnings("ignore")


# 基础日志配置：方便你看到脚本跑到哪一步
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


# 本地路径（改成你当前 news_rec 目录下的结构）
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data_raw"
SAVE_PATH = BASE_DIR / "temp_results"
SAVE_PATH.mkdir(parents=True, exist_ok=True)


def reduce_mem(df: pd.DataFrame) -> pd.DataFrame:
    """可选：压缩数值列内存占用（本 baseline 里不是必须，但保留方便后续扩展）"""
    start_time = time.time()
    start_mem = df.memory_usage().sum() / 1024**2
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]

    for col in df.columns:
        col_type = df[col].dtypes
        if str(col_type) not in numerics:
            continue

        c_min = df[col].min()
        c_max = df[col].max()
        if pd.isnull(c_min) or pd.isnull(c_max):
            continue

        if str(col_type).startswith("int"):
            if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                df[col] = df[col].astype(np.int8)
            elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                df[col] = df[col].astype(np.int16)
            elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                df[col] = df[col].astype(np.int32)
            else:
                df[col] = df[col].astype(np.int64)
        else:
            if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                df[col] = df[col].astype(np.float16)
            elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                df[col] = df[col].astype(np.float32)
            else:
                df[col] = df[col].astype(np.float64)

    end_mem = df.memory_usage().sum() / 1024**2
    logger.info(
        "reduce_mem: %.2fMB -> %.2fMB (%.1f%%), cost %.2fs",
        start_mem,
        end_mem,
        100 * (start_mem - end_mem) / max(start_mem, 1e-9),
        time.time() - start_time,
    )
    return df


def get_all_click_sample(data_path: Path, sample_users: int = 10000) -> pd.DataFrame:
    """
    debug 模式：按用户采样一部分训练数据（后续你调试可以用）
    """
    all_click = pd.read_csv(data_path / "train_click_log.csv")
    all_user_ids = all_click["user_id"].unique()
    sample_user_ids = np.random.choice(all_user_ids, size=sample_users, replace=False)
    all_click = all_click[all_click["user_id"].isin(sample_user_ids)]
    all_click = all_click.drop_duplicates(["user_id", "click_article_id", "click_timestamp"])
    return all_click.reset_index(drop=True)


def get_all_click_df(data_path: Path, offline: bool = True) -> pd.DataFrame:
    """
    读取点击日志数据
    - offline=True: 只用训练集（适合线下验证/先看结构）
    - offline=False: 训练集 + 测试集A 合并（适合生成线上提交）

    这里保留了小样本切片，方便你本地先跑通。
    后续想跑更多数据，把 [:10000] / [:20000] 放大即可。
    """
    if offline:
        all_click = pd.read_csv(data_path / "train_click_log.csv")[:20000]
    else:
        trn_click = pd.read_csv(data_path / "train_click_log.csv")[:10000]
        tst_click = pd.read_csv(data_path / "testA_click_log.csv")[:10000]
        all_click = pd.concat([trn_click, tst_click], ignore_index=True)

    all_click = all_click.drop_duplicates(["user_id", "click_article_id", "click_timestamp"])
    all_click = all_click.reset_index(drop=True)
    return all_click


def get_user_item_time(click_df: pd.DataFrame) -> dict:
    """
    根据点击时间获取用户的点击文章序列
    返回:
        {user_id: [(click_article_id, click_timestamp), ...], ...}
    """
    click_df = click_df.sort_values("click_timestamp")

    def make_item_time_pair(df: pd.DataFrame):
        return list(zip(df["click_article_id"], df["click_timestamp"]))

    user_item_time_df = (
        click_df.groupby("user_id")[["click_article_id", "click_timestamp"]]
        .apply(make_item_time_pair)
        .reset_index()
        .rename(columns={0: "item_time_list"})
    )
    user_item_time_dict = dict(
        zip(user_item_time_df["user_id"], user_item_time_df["item_time_list"])
    )
    return user_item_time_dict


def get_item_topk_click(click_df: pd.DataFrame, k: int):
    """获取点击最多的 TopK 文章（热门补全用）"""
    return click_df["click_article_id"].value_counts().index[:k].tolist()


def itemcf_sim(df: pd.DataFrame, save_path: Path) -> dict:
    """
    计算 ItemCF 文章相似度矩阵（i2i）
    """
    logger.info("Step 1/4: build user-item-time dict")
    user_item_time_dict = get_user_item_time(df)

    logger.info("Step 2/4: compute item co-occurrence similarity")
    i2i_sim = {}
    item_cnt = defaultdict(int)

    # tqdm 默认显示；如果你觉得刷屏，可以加 disable=True
    for _, item_time_list in tqdm(user_item_time_dict.items(), desc="itemcf_sim"):
        for i, _ in item_time_list:
            item_cnt[i] += 1
            i2i_sim.setdefault(i, {})
            for j, _ in item_time_list:
                if i == j:
                    continue
                i2i_sim[i].setdefault(j, 0.0)
                # 用户历史越长，对单个共现贡献越小（常见简单惩罚）
                i2i_sim[i][j] += 1 / math.log(len(item_time_list) + 1)

    logger.info("Step 3/4: normalize i2i similarity")
    i2i_sim_norm = {}
    for i, related_items in i2i_sim.items():
        i2i_sim_norm[i] = {}
        for j, wij in related_items.items():
            i2i_sim_norm[i][j] = wij / math.sqrt(item_cnt[i] * item_cnt[j])

    pkl_path = save_path / "itemcf_i2i_sim.pkl"
    with open(pkl_path, "wb") as f:
        pickle.dump(i2i_sim_norm, f)
    logger.info("Step 4/4: saved i2i sim -> %s", pkl_path)
    return i2i_sim_norm


def item_based_recommend(
    user_id,
    user_item_time_dict: dict,
    i2i_sim: dict,
    sim_item_topk: int,
    recall_item_num: int,
    item_topk_click: list,
):
    """
    基于 ItemCF 的单用户召回
    返回:
        [(item_id, score), ...] （按 score 降序截断）
    """
    user_hist_items = user_item_time_dict[user_id]  # [(item, ts), ...]
    user_hist_item_ids = {item for item, _ in user_hist_items}

    item_rank = {}
    for _, (i, _) in enumerate(user_hist_items):
        if i not in i2i_sim:
            continue

        for j, wij in sorted(i2i_sim[i].items(), key=lambda x: x[1], reverse=True)[:sim_item_topk]:
            # 不推荐用户已经点过的文章
            if j in user_hist_item_ids:
                continue
            item_rank.setdefault(j, 0.0)
            item_rank[j] += wij

    # 不足 recall_item_num，用热门文章补全
    if len(item_rank) < recall_item_num:
        for idx, item in enumerate(item_topk_click):
            if item in user_hist_item_ids or item in item_rank:
                continue
            item_rank[item] = -idx - 100.0  # 给一个很小的分数，确保补全项排在后面
            if len(item_rank) == recall_item_num:
                break

    item_rank = sorted(item_rank.items(), key=lambda x: x[1], reverse=True)[:recall_item_num]
    return item_rank


def build_recall_df(
    all_click_df: pd.DataFrame,
    i2i_sim: dict,
    sim_item_topk: int = 10,
    recall_item_num: int = 10,
) -> pd.DataFrame:
    """
    给每个用户做 ItemCF 召回，输出:
        user_id, click_article_id, pred_score
    """
    logger.info("Build recall candidates for each user")
    user_recall_items_dict = defaultdict(dict)
    user_item_time_dict = get_user_item_time(all_click_df)
    item_topk_click = get_item_topk_click(all_click_df, k=50)

    for user in tqdm(all_click_df["user_id"].unique(), desc="recall_users"):
        user_recall_items_dict[user] = item_based_recommend(
            user_id=user,
            user_item_time_dict=user_item_time_dict,
            i2i_sim=i2i_sim,
            sim_item_topk=sim_item_topk,
            recall_item_num=recall_item_num,
            item_topk_click=item_topk_click,
        )

    user_item_score_list = []
    for user, items in user_recall_items_dict.items():
        for item, score in items:
            user_item_score_list.append([user, item, score])

    recall_df = pd.DataFrame(
        user_item_score_list, columns=["user_id", "click_article_id", "pred_score"]
    )
    return recall_df


def submit(recall_df: pd.DataFrame, save_path: Path, topk: int = 5, model_name: str = "itemcf_baseline"):
    """
    生成提交文件（user_id + article_1...article_5）
    """
    # 先按用户、分数降序排
    recall_df = recall_df.sort_values(["user_id", "pred_score"], ascending=[True, False]).copy()

    # 给每个用户内部编号 rank=1,2,3...
    recall_df["rank"] = recall_df.groupby("user_id").cumcount() + 1

    # 保证每个用户召回数够 topk
    cnt = recall_df.groupby("user_id")["click_article_id"].count()
    assert cnt.min() >= topk, f"存在用户召回不足 {topk} 篇，最少只有 {cnt.min()} 篇"

    topk_df = recall_df[recall_df["rank"] <= topk][["user_id", "click_article_id", "rank"]]
    submit_df = topk_df.pivot(index="user_id", columns="rank", values="click_article_id").reset_index()

    # 重命名列，适配 sample_submit.csv 风格
    rename_map = {i: f"article_{i}" for i in range(1, topk + 1)}
    submit_df = submit_df.rename(columns=rename_map)

    save_name = save_path / f"{model_name}_{datetime.today().strftime('%m-%d')}.csv"
    submit_df.to_csv(save_name, index=False, header=True)
    logger.info("submission saved -> %s", save_name)
    return save_name


def main():
    logger.info("=== ItemCF Baseline Start ===")
    logger.info("BASE_DIR = %s", BASE_DIR)
    logger.info("DATA_PATH = %s", DATA_PATH)
    logger.info("SAVE_PATH = %s", SAVE_PATH)

    # 先做文件存在性检查，避免路径错了才开始跑
    required = ["train_click_log.csv", "testA_click_log.csv", "articles.csv"]
    for name in required:
        p = DATA_PATH / name
        if not p.exists():
            raise FileNotFoundError(f"缺少数据文件: {p}")

    # 读取（合并）点击日志：offline=False 表示 train + testA（适合生成提交）
    all_click_df = get_all_click_df(DATA_PATH, offline=False)
    logger.info("all_click_df shape = %s", all_click_df.shape)
    logger.info("all_click_df columns = %s", all_click_df.columns.tolist())
    logger.info("all_click_df head:\n%s", all_click_df.head(3).to_string(index=False))

    # 计算 i2i 相似度
    i2i_sim = itemcf_sim(all_click_df, SAVE_PATH)

    # 生成召回表
    recall_df = build_recall_df(
        all_click_df=all_click_df,
        i2i_sim=i2i_sim,
        sim_item_topk=10,
        recall_item_num=10,
    )
    logger.info("recall_df shape = %s", recall_df.shape)
    logger.info("recall_df head:\n%s", recall_df.head(5).to_string(index=False))

    # 从召回结果里筛出 testA 用户，生成提交文件
    tst_click = pd.read_csv(DATA_PATH / "testA_click_log.csv")[:10000]
    tst_users = tst_click["user_id"].unique()
    tst_recall = recall_df[recall_df["user_id"].isin(tst_users)].copy()
    logger.info("tst_recall shape = %s", tst_recall.shape)

    submit_path = submit(tst_recall, SAVE_PATH, topk=5, model_name="itemcf_baseline")
    logger.info("Done. You can inspect submission: %s", submit_path)


if __name__ == "__main__":
    main()
