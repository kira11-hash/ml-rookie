# Day6 执行单（2026-02-21）

> 今日只做一件事：MNIST 验收。不开新坑，不并行其它任务。

## 1. 开始前（5分钟）
1. 打开终端并进入项目目录。
2. 设置环境变量：

```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

3. 跑环境检查：

```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_env_check.py"
```

## 2. 手写主任务（90-150分钟）
1. 打开：
`/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_handwrite.py`
2. 按 TODO 顺序补全：
- `get_device`
- `build_loaders`
- `build_model`
- `train_one_epoch`
- `evaluate_acc`
- `train_pipeline`
3. 运行脚本：

```bash
/usr/bin/python3 "/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_handwrite.py"
```

## 3. 卡住时处理（最多20分钟）
1. 先自己定位：
- 看报错行号
- 打印关键变量（shape/device/loss）
2. 超过20分钟再对照：
`/Users/chenqingan/Library/Mobile Documents/com~apple~CloudDocs/ml-rookie/everyday_learning/day6/day6_solution.py`

## 4. 今日验收标准（必须满足）
1. `phase1 test acc >= 92%`
2. `phase2 test acc >= 95%`
3. 输出包含：
- `final loss`
- `phase1 test acc`
- `phase2 test acc`
- `elapsed sec`
4. 你能口述：
- DataLoader 在干什么
- 为什么分类用 `CrossEntropyLoss`
- `argmax(dim=1)` 为什么能得到类别

## 5. 收尾（15分钟）
1. 在 `ml_learning_log.md` 填写 Day6 记录。
2. 将今日疑问补到 `my_leetcode_learning/wrongbook.md`（如果有）。
3. 若还有精力，只做代码整理，不开新任务。

## 6. 明日预告（2026-02-22）
- 纯复习日：回顾 Day1-Day5 和 Day6，不上新内容。
- 重点复习：函数、字典统计、正则清洗、文件IO、训练循环。
