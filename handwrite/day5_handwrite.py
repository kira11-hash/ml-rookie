"""
Day5 手写练习（必须自己填空）
主题：PyTorch 预热 + 最小训练循环
目标：在 MPS/CPU 上训练一个线性模型，拟合 y = 2x + 1
"""

import os

print("=== Day5 手写练习开始 ===")

try:
    import torch
    import torch.nn as nn
except ModuleNotFoundError:
    print("[错误] 未检测到 PyTorch。")
    print("请先安装后再运行，例如：pip3 install torch")
    raise SystemExit(1)


def get_device():
    """
    TODO 1:
    1) 如果 mps 可用，返回 torch.device("mps")
    2) 否则返回 torch.device("cpu")
    """
    return torch.device("cpu")


def make_data(device):
    """
    TODO 2:
    1) 构造 x: [[1.0], [2.0], [3.0], [4.0], [5.0]]
    2) 构造 y: y = 2*x + 1
    3) x, y 都放到 device 上
    4) 返回 x, y
    """
    x = torch.tensor([[0.0]], dtype=torch.float32, device=device)
    y = torch.tensor([[0.0]], dtype=torch.float32, device=device)
    return x, y


def train_linear(x, y, device, epochs=300, lr=0.05):
    """
    TODO 3:
    1) model = nn.Linear(1, 1).to(device)
    2) loss_fn = nn.MSELoss()
    3) optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    4) 训练循环:
       - pred = model(x)
       - loss = loss_fn(pred, y)
       - optimizer.zero_grad()
       - loss.backward()
       - optimizer.step()
    5) 返回 model, final_loss(float)
    """
    model = None
    final_loss = None
    return model, final_loss


def predict_one(model, device, x_value=4.0):
    """
    TODO 4:
    1) 构造输入 [[x_value]]
    2) 用 with torch.no_grad() 做前向
    3) 返回预测值（float）
    """
    return -999.0


torch.manual_seed(42)
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

device = get_device()
print("PyTorch version:", torch.__version__)
print("MPS available:", torch.backends.mps.is_available())
print("Using device:", device)

x, y = make_data(device)
model, final_loss = train_linear(x, y, device)
pred_4 = predict_one(model, device, 4.0)

print("x shape:", x.shape)
print("y shape:", y.shape)
print("final_loss:", final_loss)
print("predict x=4.0:", pred_4)


# 验收断言（补完 TODO 后应通过）
assert tuple(x.shape) == (5, 1), "x 形状应为 (5, 1)"
assert tuple(y.shape) == (5, 1), "y 形状应为 (5, 1)"
assert x.device.type == device.type, "x 没放到正确 device"
assert y.device.type == device.type, "y 没放到正确 device"
assert model is not None, "model 不能是 None"
assert final_loss is not None, "final_loss 不能是 None"
assert final_loss < 0.2, "loss 没降下来，检查训练循环"
assert 8.0 < pred_4 < 10.0, "x=4 的预测应接近 9"

print("\nDay5 手写练习通过。")
