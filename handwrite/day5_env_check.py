"""
Day5 环境检查脚本
用途：在开始 day5_handwrite.py 前快速确认 PyTorch/MPS 状态
"""

import os
import platform

print("=== Day5 环境检查 ===")
print("OS:", platform.platform())
print("Python:", platform.python_version())

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")
print("PYTORCH_ENABLE_MPS_FALLBACK =", os.environ.get("PYTORCH_ENABLE_MPS_FALLBACK"))

try:
    import torch
except ModuleNotFoundError:
    print("[错误] 未安装 PyTorch")
    print("先执行安装，再继续 Day5。")
    raise SystemExit(1)

print("torch version:", torch.__version__)
print("mps available:", torch.backends.mps.is_available())
print("cuda available:", torch.cuda.is_available())

if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")
print("selected device:", device)

print("\n环境检查完成。")

