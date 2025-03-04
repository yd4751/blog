# 安装
``` shell
#
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117   #gpu版本
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu #cpu版本


#环境验证
import torch  
print(torch.__version__)         # 输出 PyTorch 版本（如 2.0.1）‌
print(torch.cuda.is_available()) # 返回 True 表示 GPU 加速可用 ‌

```

# 