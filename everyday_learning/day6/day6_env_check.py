"""
Day6 环境检查：MNIST baseline
"""

import os

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

print("=== Day6 Env Check ===")

try:
    import torch
except ModuleNotFoundError:
    print("[失败] 未安装 torch")
    raise SystemExit(1)

try:
    import torchvision
except ModuleNotFoundError:
    print("[失败] 未安装 torchvision")
    raise SystemExit(1)

print("torch:", torch.__version__)
print("torchvision:", torchvision.__version__)
print("mps available:", torch.backends.mps.is_available())
print("fallback env:", os.environ.get("PYTORCH_ENABLE_MPS_FALLBACK"))
print("\n环境检查通过。")
