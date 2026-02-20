"""
Day5 参考解
主题：PyTorch 预热 + 最小训练循环
目标：在 MPS/CPU 上训练一个线性模型，拟合 y = 2x + 1
"""

import os

print("=== Day5 参考解开始 ===")

try:
    import torch
    import torch.nn as nn
except ModuleNotFoundError:
    print("[错误] 未检测到 PyTorch。")
    print("请先安装后再运行，例如：pip3 install torch")
    raise SystemExit(1)


def get_device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def make_data(device):
    x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]], dtype=torch.float32, device=device)
    y = 2 * x + 1
    return x, y


def train_linear(x, y, device, epochs=300, lr=0.05):
    model = nn.Linear(1, 1).to(device)
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)

    final_loss = None
    for _ in range(epochs):
        pred = model(x)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        final_loss = float(loss.item())
    return model, final_loss


def predict_one(model, device, x_value=4.0):
    x_test = torch.tensor([[x_value]], dtype=torch.float32, device=device)
    with torch.no_grad():
        y_pred = model(x_test)
    return float(y_pred.item())


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


assert tuple(x.shape) == (5, 1), "x 形状应为 (5, 1)"
assert tuple(y.shape) == (5, 1), "y 形状应为 (5, 1)"
assert x.device.type == device.type, "x 没放到正确 device"
assert y.device.type == device.type, "y 没放到正确 device"
assert model is not None, "model 不能是 None"
assert final_loss is not None, "final_loss 不能是 None"
assert final_loss < 0.2, "loss 没降下来，检查训练循环"
assert 8.0 < pred_4 < 10.0, "x=4 的预测应接近 9"

print("\nDay5 参考解通过。")
