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
#clash地址，选择arm64版本下载
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
# 这是服务运行的具体执行命令,可执行执行脚本的绝对路径,即对应的service start/stop/reload
ExecStart=/home/ubuntu/installer/nacos/bin/startup.sh -m standalone
ExecReload=/home/ubuntu/installer/nacos/bin/shutdown.sh
ExecStop=/home/ubuntu/installer/nacos/bin/shutdown.sh
[Install]
# 这里你没太大要求可以不管
WantedBy=multi-user.target

```

# 常用命令
``` shell
###########################################文件管理###########################################
#列出目录内容
ls #列出当前目录下的所有非隐藏文件和文件夹
ls -l #以详细列表形式显示文件和文件夹信息
ls -a #显示当前目录下包括隐藏文件在内的所有文件和文件夹

#切换工作目录
cd /path/to/directory #切换到指定目录
cd .. #返回上一级目录
cd ~ #返回当前用户的宿主目录

#创建和删除目录
mkdir new_folder #在当前目录下创建一个名为new_folder的新目录。
rmdir empty_folder #删除一个空目录。注意，如果目录不为空，则无法使用此命令。

#删除文件
rm file.txt #删除当前目录下的file.txt文件。
rm -r directory #递归删除directory目录及其所有内容。使用-f选项可以强制删除，不提示确认。

#复制和移动文件
cp file1.txt file2.txt #将file1.txt复制为file2.txt。
mv file.txt new_location/file.txt #将file.txt移动到new_location目录下。
mv old_name.txt new_name.txt #将文件old_name.txt重命名为new_name.txt。

###########################################磁盘管理###########################################
#查看磁盘使用情况
df -h #以人类可读的方式（如KB、MB、GB等）显示磁盘使用情况
df -h --block-size=g #以GB为单位显示磁盘使用情况
#查看目录占用空间
du -sh /path/to/directory #显示指定目录的总大小

###########################################用户管理###########################################
#查看当前用户
whoami：显示当前登录的用户名。
#添加新用户
sudo adduser newuser #添加一个名为newuser的新用户。系统会提示设置密码和填写用户信息
#修改用户密码
sudo passwd username #修改指定用户的密码
#删除用户
sudo userdel -r username #删除指定用户及其主目录和文件

###########################################软件管理###########################################
#更新软件源列表
sudo apt update 或 sudo apt-get update #更新Ubuntu的软件源列表
#安装软件
sudo apt install package_name 或 sudo apt-get install package_name #安装指定软件包
#删除软件
sudo apt remove package_name 或 sudo apt-get remove package_name #删除已安装的软件包
#升级软件
sudo apt upgrade 或 sudo apt-get upgrade #升级所有已安装的可升级软件包

###########################################进程管理###########################################
#查看进程
ps aux
    a: 显示所有用户的进程（包括其他用户的进程）。
    u：以用户为中心的格式显示进程信息。这通常包括用户（USER）、PID（进程ID）、CPU使用率、内存使用率、虚拟内存大小、常驻内存大小、TTY（终端类型）、STAT（进程状态）、START（进程启动时间）、TIME（CPU时间）和COMMAND（命令名/命令行）。
    x：显示没有控制终端的进程。
ps -ef
    e：显示所有进程。
    f：完整格式显示，通常包括UID（用户ID）、PID、PPID（父进程ID）、C（CPU使用率）、STIME（启动时间）、TTY、TIME和CMD（命令）。这个格式更侧重于进程的层级关系。
ps -l
    长格式显示，提供关于进程的详细信息，但不如 aux 或 ef 那么详细。它通常包括F（标志）、UID、PID、PPID、C、PRI（优先级）、NI（nice值）、ADDR（内存地址）、SZ（使用的内存大小）、WCHAN（等待的通道）、TTY、TIME和CMD。
ps -p PID
    通过进程ID（PID）显示特定进程的信息。例如，ps -p 1234 会显示PID为1234的进程的信息。
ps -C CMD
    通过命令名显示进程信息。例如，ps -C bash 会显示所有bash进程的信息。
ps -L
    显示线程信息。这个选项通常与 -e 或特定PID一起使用，以显示所有线程或特定进程的线程。
ps -o FORMAT
    自定义输出格式。FORMAT 是一个逗号分隔的列表，指定了要显示的字段。例如，ps -o pid,user,cmd 只显示进程ID、用户和命令。
ps -t TTY
    显示与特定终端关联的进程。例如，ps -t pts/0 会显示与pts/0终端关联的所有进程。

#杀死进程
kill
    -l 或 --list：列出所有可用的信号名称和对应的数字。
    -s SIGNAL：指定要发送的信号名称或编号。
    -p 打印进程的状态，不发送信号。
    -0 检查进程是否存在，不发送信号。如果进程存在，则命令返回成功；否则返回失败。

###########################################其它命令###########################################
#查看当前目录的绝对路径
pwd #显示当前所在目录的绝对路径
#实时显示系统进程资源占用情况
top #显示当前系统中进程的CPU、内存等使用情况。按q键退出
#查看内存使用情况
free -m #以兆字节（MB）为单位显示内存使用情况，包括总内存、已使用内存、空闲内存等信息
#查找文件
find /path -name "filename" #在指定路径下查找名为filename的文件或目录
#查看IP地址
ip a #显示当前系统的IP地址信息。
#关机和重启
sudo shutdown -h now #立即关闭系统。
sudo shutdown -r now #立即重启系统。
```