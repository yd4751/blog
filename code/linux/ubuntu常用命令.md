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

#Debian/Ubuntu 系统底层的软件包管理工具，支持 .deb 格式软件包的安装、卸载、查询及配置‌
#直接操作本地 .deb 文件，无需联网
#不自动处理依赖关系，需配合 apt 等工具解决依赖冲突‌
dpkg
    -i package.deb  # 安装本地 .deb 文件
    -r package_name    # 卸载软件包但保留配置文件‌
    -P package_name    # 完全卸载（包括配置文件）‌
    -l                      # 列出所有已安装的包及状态
    -l | grep keyword       # 按关键词过滤已安装的包‌
    -s package_name         # 查看包的详细信息
    -L package_name         # 列出包安装的所有文件路径‌
    --unpack package.deb  # 解压 .deb 文件但不配置‌
    --configure package   # 手动配置已解压的包‌
    -S /path/to/file        # 根据文件路径反向查找所属包‌
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

#服务控制
systemctl
    -t：指定 Unit 类型（如 service、socket）‌
    -a：显示所有单元（包括非活动状态）
    --state：过滤特定状态的单元‌

systemctl start <服务名>    # 启动服务‌
systemctl stop <服务名>     # 停止服务‌
systemctl restart <服务名>  # 重启服务‌
systemctl reload <服务名>  # 重新加载配置（不中断服务）‌
systemctl status <服务名>  # 查看服务状态（含日志摘要）‌
systemctl list-units       # 显示所有活跃单元‌
systemctl list-dependencies <服务名>  # 查看服务依赖关系‌
systemctl enable <服务名>   # 启用开机自启‌
systemctl disable <服务名>  # 禁用开机自启‌
systemctl is-enabled <服务名>  # 检查是否已启用自启‌
systemctl reboot    # 重启系统‌
systemctl poweroff  # 关机‌
systemctl suspend   # 挂起（睡眠模式）‌

系统级服务：/etc/systemd/system/（优先级最高）‌
软件包默认配置：/usr/lib/systemd/system/‌

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

###########################################网络管理###########################################
#用来查看系统的网络连接、路由表、接口统计等信息。
netstat 
    -t：显示TCP连接
    -u：显示UDP连接
    -l：仅显示监听状态的端口
    -n：以数字形式显示地址和端口号，而不是尝试解析为域名

#另一个用于查看套接字统计信息的工具，它是 netstat 的现代替代品，提供了更快的执行速度和更多的信息。
ss
    -t：显示TCP连接
    -u：显示UDP连接
    -l：仅显示监听状态的端口
    -n：以数字形式显示地址和端口号

#lsof（list open files）是一个列出当前系统打开文件的工具。由于在Unix和类Unix系统中一切皆文件，网络连接也不例外，因此它也可以用来查看哪些进程打开了哪些端口
lsof
    -i：显示网络连接信息
    -P：不要将端口号转换为名字（例如，显示数字端口而不是服务名）
    -n：不要将IP地址转换为名字（例如，显示数字IP地址而不是主机名）

#是一个网络扫描工具，可以用来发现网络上的设备和服务。它也可以用来查看本地监听的端口
nmap 

#用于在命令行界面与Web服务器进行数据传输。它支持多种协议，如HTTP、HTTPS、FTP等
curl [options] [URL]
    -A/--user-agent #设置用户代理字符串发送给服务器。
    -b/--cookie #指定cookie字符串或读取cookie的文件位置。
    -c/--cookie-jar #操作结束后将cookie写入指定文件。
    -d/--data #以POST方式传送数据。
    -D/--dump-header #将响应头信息写入指定文件。
    -e/--referer #设置来源网址。
    -f/--fail #连接失败时不显示HTTP错误。
    -H/--header #添加自定义请求头。
    -I/--head #只显示响应头信息。
    -L/--location #跟随重定向。
    -o/--output #将响应内容保存到指定文件，而不是标准输出。
    -O/--remote-name #将响应内容保存到与远程文件名相同的文件中。
    -s/--silent #静默模式，不输出任何信息。
    -u/--user #<user[:password]>：设置服务器的用户和密码。
    -v/--verbose #显示详细的信息，包括请求和响应头。这对于问题排查和了解HTTP协议原理非常有用。
    -x/--proxy #<host[:port]>：设置代理服务器及其端口。
    -#/--progress-bar #显示进度条，表示当前的传输状态。

#命令行环境下使用的网络下载工具，它支持HTTP、HTTPS和FTP协议
wget [option] [URL]
    -O #选项指定下载文件的保存名称
    --limit-rate #选项限制下载速度
    -c #默认会尝试断点续传。可以使用-c选项明确指定这一功能
    -b #选项让wget在后台运行
    --proxy-host #选项设置代理服务器
    --proxy-port #选项设置代理服务器
    --proxy-user #设置代理服务器的用户名
    --proxy-password #设置代理服务器的密码
    --timeout #选项设置连接超时时间（以秒为单位）
    -O #将内容直接输出到标准输出（通常是终端）
    -r/--recursive #选项递归地下载指定网页中的所有链接
    -l #选项限制递归深度
    --user-agent #选项伪装或定制用户代理
    --tries #选项设置重试次数
    -Q/--quota #选项限制总下载文件大小
    -accept #选项指定要下载的文件类型
    -reject #选项排除要下载的文件类型
    -cookies on #启用Cookies支持
    -load-cookies filename #加载
    -save-cookies filename #保存
    
#软件包管理
apt 
    update   #更新软件源列表
    upgrade  # 仅升级包，保留旧版本依赖
    full-upgrade  # 升级包并移除废弃依赖
    install <包名>           # 安装单个包
    install <包1> <包2>      # 同时安装多个包‌
    remove <包名>           # 移除软件包但保留配置文件
    purge <包名>            # 彻底删除软件包及其配置文件‌
    search <关键词>             # 搜索仓库中匹配的包名
    show <包名>                 # 查看包的版本、依赖、大小等详细信息‌
    autoremove     # 删除自动安装且不再使用的依赖
    autoclean      # 清理旧版本软件包缓存（保留最新版本）‌
    list --installed     # 显示所有已安装的包
    list --all-versions  # 查看所有已安装包的版本信息‌
    install <包名>=<版本号>  # 安装特定版本
    install -y <包名>       # 自动确认操作

#软件包管理
snapd
    version  # 显示 snapd 和系统版本‌
    set system proxy.http="http://代理IP:端口"  # 全局生效‌:ml-citation{ref="5" data="citationList"}
    set system proxy.https="http://代理IP:端口"
    find <关键词> #从 Snap Store 查找软件
    install <应用名> #安装指定应用
    list #显示所有已安装
    refresh <应用名> #更新单个应用
    refresh #更新全部应用
    remove <应用名> #删除指定应用‌
    info <应用名> #显示应用描述、版本及权限配置‌
    run <应用名> #启动已安装的 Snap 应用‌
    --channel=候选通道  #通道控制  sudo snap install <应用名> --channel=候选通道
    connections <应用名>  # 查看应用的接口权限‌
    disconnect <应用名>:<接口>  # 禁用特定权限（如摄像头）‌
    revert <应用名>      # 恢复到上一个版本‌
##应用数据路径
/var/snap/<应用名>‌
##用户数据路径
~/snap/<应用名>‌
```

