"""
Day6 手写练习（Week1 启动版）
主题：MNIST baseline（MLP）
目标：
1) 跑通训练与评估（MPS 优先，失败回退 CPU）
2) 阶段1测试集准确率 > 92%
3) 阶段2测试集准确率 > 95%
4) 记录 final loss / test acc / 训练耗时
"""

import os
import time
from pathlib import Path

print("=== Day6 start: MNIST baseline ===")

try:
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
    from torchvision import datasets, transforms
except ModuleNotFoundError as e:
    print("[错误] 缺少依赖:", e)
    print("请先安装：/usr/bin/python3 -m pip install torch torchvision")
    raise SystemExit(1)


def get_device(prefer_mps=True):
    """
    TODO 1:
    - prefer_mps=True 且 MPS 可用 -> torch.device("mps")
    - 否则 -> torch.device("cpu")
    """
    if prefer_mps and torch.backends.mps.is_available():
        device=torch.device("mps")
    else:
        device = torch.device("cpu")
    return device

def build_loaders(data_dir, train_batch_size=128, test_batch_size=512):
    """
    TODO 2:
    1) 定义 transform = transforms.ToTensor()
    2) 构造 MNIST 训练集和测试集（download=True）
    3) 构造 train_loader / test_loader
       - train: shuffle=True
       - test: shuffle=False
    4) return train_loader, test_loader
    """
    transform = transforms.ToTensor()

    train_ds = datasets.MNIST(root=str(data_dir),train=True,transform=transform,download=True)
    test_ds=datasets.MNIST(root=str(data_dir),train=False,transform=transform,download=True)

    train_loader=DataLoader(train_ds,batch_size=train_batch_size,shuffle=True)
    test_loader=DataLoader(test_ds,batch_size=test_batch_size,shuffle=False)

    return train_loader,test_loader

def build_model(device):
    """
    TODO 3:
    构建简单 MLP：
    nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 128),
        nn.ReLU(),
        nn.Linear(128, 10),
    )
    并放到 device 上
    """
    model=nn.Sequential(
        nn.Flatten(),
        nn.Linear(28*28,128),
        nn.ReLU(),
        nn.Linear(128,10),
    )
    return model.to(device)


def train_one_epoch(model, train_loader, optimizer, loss_fn, device):
    """
    TODO 4:
    1) model.train()
    2) 遍历 train_loader：
       - xb, yb 搬到 device
       - pred = model(xb)
       - loss = loss_fn(pred, yb)
       - optimizer.zero_grad()
       - loss.backward()
       - optimizer.step()
    3) 返回该 epoch 的平均 loss（float）
    """
    model.train()
    total_loss=0
    total_count=0

    for xb,yb in train_loader:
        xb=xb.to(device)
        yb=yb.to(device)

        logits=model(xb)
        loss=loss_fn(logits,yb)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        bs=xb.size(0)
        total_loss += float(loss.item())*bs
        total_count += bs

    return total_loss/max(total_count,1)


def evaluate_acc(model, test_loader, device):
    """
    TODO 5:
    1) model.eval()
    2) with torch.no_grad():
       - 前向
       - pred_label = logits.argmax(dim=1)
       - 统计 correct / total
    3) 返回准确率（百分比 float，例如 96.35）
    """
    model.eval()
    correct = 0
    total = 0

    for xb,yb in test_loader:
        xb= xb.to(device)
        yb= yb.to(device)

        with torch.no_grad():

            logits=model(xb)
            pred_label = logits.argmax(dim=1)
            correct += (pred_label==yb).sum().item()
            total += int(yb.numel())

    return 100.0*correct/max(total,1)


def train_pipeline(device, data_dir, phase1_epochs=1, phase2_epochs=1, lr=1e-3):
    """
    TODO 6:
    1) 构造 loader / model / loss_fn / optimizer(Adam)
    2) 训练 phase1_epochs，得到 phase1_acc
    3) 再训练 phase2_epochs，得到 phase2_acc
    4) 记录 final_loss 和 elapsed_sec
    5) 返回字典：
       {
         "device": device.type,
         "final_loss": ...,
         "phase1_acc": ...,
         "phase2_acc": ...,
         "elapsed_sec": ...,
       }
    """
    train_loader, test_loader = build_loaders(data_dir)
    model = build_model(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    start = time.perf_counter()
    final_loss = None

    for _ in range(phase1_epochs):
        final_loss = train_one_epoch(model, train_loader, optimizer, loss_fn, device)
    phase1_acc = evaluate_acc(model, test_loader, device)

    for _ in range(phase2_epochs):
        final_loss = train_one_epoch(model, train_loader, optimizer, loss_fn, device)
    phase2_acc = evaluate_acc(model, test_loader, device)

    elapsed = time.perf_counter() - start

    return {
        "device": device.type,
        "final_loss": float(final_loss),
        "phase1_acc": float(phase1_acc),
        "phase2_acc": float(phase2_acc),
        "elapsed_sec": float(elapsed),
    }


def main():
    torch.manual_seed(42)
    os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

    base_dir = Path(__file__).resolve().parent
    data_dir = base_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    preferred = get_device(prefer_mps=True)
    print("PyTorch version:", torch.__version__)
    print("MPS available:", torch.backends.mps.is_available())
    print("Preferred device:", preferred)

    try:
        metrics = train_pipeline(preferred, data_dir)
    except RuntimeError as e:
        if preferred.type == "mps":
            print("[警告] MPS 训练失败，回退 CPU：", e)
            cpu_device = torch.device("cpu")
            metrics = train_pipeline(cpu_device, data_dir)
        else:
            raise

    print("\n=== Day6 Metrics ===")
    print("device used:", metrics["device"])
    print("final loss:", metrics["final_loss"])
    print("phase1 test acc (%):", metrics["phase1_acc"])
    print("phase2 test acc (%):", metrics["phase2_acc"])
    print("elapsed sec:", metrics["elapsed_sec"])

    # 验收目标
    assert metrics["phase1_acc"] >= 92.0, "Phase1 准确率未达到 92%"
    assert metrics["phase2_acc"] >= 95.0, "Phase2 准确率未达到 95%"
    assert metrics["final_loss"] < 0.35, "final loss 偏高，检查训练循环"

    print("\nDay6 手写练习通过。")


if __name__ == "__main__":
    main()
