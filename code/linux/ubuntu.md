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