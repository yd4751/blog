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

# clash安装
``` shell
#clash地址，选择amd64版本下载
https://github.com/DustinWin/proxy-tools/releases/tag/Clash-Premium

#此方式下载的是base64加密的数据，需要解密后拷贝到.yaml文件中
wget -O config.yaml https://xxx/xxx 

#配置代理,clash默认使用7890端口
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
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

```