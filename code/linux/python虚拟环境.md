# 核心作用
* ‌隔离依赖‌：避免不同项目间的包版本冲突，解决系统环境与开发环境冲突问题（如 externally-managed-environment 错误）
*‌ 权限安全‌：无需 sudo 即可安装包，降低误操作系统级 Python 的风险‌

# 创建方法
``` shell
#方法1 使用 venv（Python 内置工具）
sudo apt update && sudo apt install python3.12-venv  # 以 Python 3.12 为例‌
python3 -m venv ~/myproject_venv  # 在用户目录下创建名为 myproject_venv 的虚拟环境‌

#方法2 使用 virtualenv（第三方工具）
sudo apt install python3-virtualenv  # 通过系统包管理器安装‌
virtualenv ~/myproject_venv --python=python3.12  # 指定 Python 版本‌

```

# 激活和使用
``` shell
source ~/myproject_venv/bin/activate  # 激活（Bash/Zsh）‌
#安装依赖
pip install torch numpy  # 在激活的虚拟环境中自由安装包‌
#退出
deactivate  # 返回系统默认环境‌

```

