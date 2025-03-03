# 安装

``` shell
#选择安装包
‌Anaconda‌ #包含 Python 和 1500+ 预装科学计算包，适合全栈开发‌
https://www.anaconda.com/download #官网
https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ #清华镜像
‌Miniconda‌ #仅含 Conda 和 Python，轻量级，适合自定义环境‌
https://www.anaconda.com/download/ #官网
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ #清华镜像

注意：
Miniconda‌3默认绑定 ‌Python 3.x‌ 版本，安装后直接提供 Python 3 环境‌
Miniconda‌默认绑定 ‌Python 2.x‌ 版本，安装后直接提供 Python 2 环境‌
国内镜像容易封IP，有代理直接官网下就行

#验证安装
conda --version  # 查看版本

#配置镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes  # 显示下载源地址

# 升级
conda update conda
```

# 环境管理
``` shell
#创建
conda create -n myenv python=3.9  # -n 指定环境名‌

#删除
conda remove -n myenv --all  # 彻底删除环境

#激活
conda activate myenv  # Windows/Linux/macOS 通用‌

#退出
conda deactivate‌

#导出到yml
conda env export > environment.yml  # 包含完整包信息‌

#从yml加载
conda env create -f environment.yml‌

#查看所有环境
conda info --envs  # 显示环境路径和状态‌

#查看环境存储路径
conda info --base‌

#清理缓存
conda clean --all  # 释放磁盘空间‌

#修复损坏环境
conda repair --env myenv  # 解决依赖冲突或环境损坏‌

```

# 包管理
``` shell
#安装包
conda install numpy=1.21.2  #指定版本包 精确版本控制‌
conda install pandas scikit-learn  #多个包 自动解析依赖‌
#卸载包
conda remove numpy‌
#更新包
conda update numpy‌
#列出已当前环境已安装包
conda list‌

```

# 注意
* 路径隔离‌：Conda 环境默认存储在用户目录下，与系统 Python 完全隔离‌
* 混合安装风险‌：避免在 Conda 环境中混用 pip 安装包，可能导致依赖冲突‌

# 问题
* CondaHTTPError: HTTP 403 FORBIDDEN   
获取http返回会发现提示:"我们检测到您所在的子网和/或所使用的客户端存在大量下载某些较大二进制文件的行为，为保证用户的正常使用，我们阻断了此类请求"
这是镜像站把ip封了
1、换源或者切换网络一般可以解决
2、我直接用代理了，删除所有镜像源配置
