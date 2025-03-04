# 查看系统版本
``` shell
cat /etc/issue
# Ubuntu 20.04.3 LTS \n \l
# 该信息可被手动修改，系统升级会导致于lsb_realease信息不一致

uname -a
# Linux bighat 6.8.0-48-generic #48-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 27 14:04:52 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

cat /proc/version
# Linux version 6.8.0-48-generic (buildd@lcy02-amd64-010) (x86_64-linux-gnu-gcc-13 (Ubuntu 13.2.0-23ubuntu4) 13.2.0, GNU ld (GNU Binutils for Ubuntu) 2.42) #48-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 27 14:04:52 UTC 2024

lsb_release -a
#该命令从 /etc/lsb-release 或 /etc/os-release 等文件中读取信息，这些文件由发行版官方维护，通常更准确且不会被手动修改。
#No LSB modules are available.
#Distributor ID:	Ubuntu
#Description:	Ubuntu 24.04.1 LTS
#Release:	24.04
#Codename:	noble
```
# 查看显卡型号
``` shell
nvidia-smi -L  # 输出示例：`GPU 0: NVIDIA GeForce RTX 3050`‌
nvidia-smi  # 显示显存、驱动版本、温度等详细信息‌
sudo lshw -C display  # 输出显卡制造商、型号、驱动等详细信息‌
sudo lshw -C display | grep -i product  # 直接提取型号信息‌

```

# 环境配置
``` shell
#全局环境配置 重启生效
sudo vi /etc/environment
```
# clash安装
``` shell
#clash地址，选择amd64版本下载
https://github.com/DustinWin/proxy-tools/releases/tag/Clash-Premium

#默认yaml路径
~/.config/clash/config.yaml

#此方式下载的是base64加密的数据，需要解密后拷贝到.yaml文件中
wget -O config.yaml https://xxx/xxx 

#配置代理,clash默认使用7890端口
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890

#有个问题
ubuntu不知道怎么使用订阅(下载下来的内容是base64加密的，解密后还有base64加密内容),windows下可以直接用，不知道ubuntu命令是要如何操作
```

# 自定义服务
* 流程  
``` shell
#Ubuntu18.04版本之后，就采用了systemctl来控制开机自启动服务
# 新建服务文件
/etc/systemd/system/myselfTest.service

#重新加载service服务
sudo systemctl daemon-reload	

# 启用服务
sudo systemctl enable myselfTest.service		

# 查看启用状态
sudo systemctl is-enabled myselfTest.service		
# 尝试手动启动服务，看是否能正常运行
service myselfTest start		
# 查看服务运行状态
service myselfTest status	
# 手动停止服务	
service myselfTest stop		

```
* 服务配置示例  
``` shell
[Unit]
# 描述，随你怎么写
Description=Cclient desktop virtualization service
After=network.target

# 这里是关键
[Service]
# 后台运行模式,服务类型，具体可以自行百度，设置成自己想要的
Type=forking
# 所属用户
#User=szyd
# 所属组
#Group=szyd
# 重启
#Restart=always
TimeoutSec=0
# 配置重新启动服务之前的睡眠时间,重启频率,比如某次异常后，等待5(s)再进行启动，默认值0.1(s)
#RestartSec=60
#设置环境变量
#Environment=MY_VAR1=value1
# 这是服务运行的具体执行命令,可执行执行脚本的绝对路径,即对应的service start/stop/reload
ExecStart=/home/ubuntu/installer/nacos/bin/startup.sh -m standalone
ExecReload=/home/ubuntu/installer/nacos/bin/shutdown.sh
ExecStop=/home/ubuntu/installer/nacos/bin/shutdown.sh
[Install]
# 这里你没太大要求可以不管
WantedBy=multi-user.target

#
系统级服务：/etc/systemd/system/（优先级最高）‌
软件包默认配置：/usr/lib/systemd/system/‌
#Type字段说明
‌simple‌：默认类型，服务进程不会fork，直接在前台运行，适用于不需要后台化的服务。
‌forking‌：服务进程会fork，父进程退出后子进程成为主进程，需指定PIDFile。
‌oneshot‌：执行一次性任务，完成后退出，常用于初始化脚本。
‌dbus‌：服务需要在D-Bus上获取一个名称后，才视为启动成功。
‌notify‌：服务通过sd_notify()函数发送通知，告知systemd已就绪。
‌idle‌：延迟服务启动，直到其他任务完成，适合低优先级服务
```

# 驱动安装
``` shell
#禁用 Nouveau 驱动
sudo vi /etc/modprobe.d/blacklist-nouveau.conf 
#添加以下内容，保存退出
blacklist nouveau  
options nouveau modeset=0  
#更新内核配置
sudo update-initramfs -u
#重启系统并验证
sudo reboot  
lsmod | grep nouveau  # 若无输出则成功
#安装编译依赖
sudo apt update 
sudo apt install gcc make libelf-dev -y     
#卸载旧驱动（如有）
sudo apt purge nvidia-*
#关闭图形界面服务(如有)
sudo service lightdm stop
#安装
sudo chmod +x NVIDIA-Linux-*.run # 添加可执行权限 ‌
sudo ./NVIDIA-Linux-*.run --no-opengl-files --no-x-check  # 关键参数避免冲突
# ‌重启并验证驱动
sudo reboot
nvidia-smi  # 显示 GPU 信息即成功
```

# 问题记录
* pip install torch 报错 error: externally-managed-environment
``` shell
此错误表示当前 Python 环境由系统包管理器（如 apt、pacman 或 brew）严格管理，直接使用 pip 安装可能破坏系统依赖一致性‌
解决:
python3 -m venv myenv         # 创建虚拟环境目录
source myenv/bin/activate    # 激活（Linux/macOS）
pip install torch
```