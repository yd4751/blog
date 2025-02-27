# 一、基础结构‌

## ‌指令顺序与注释‌

必须‌以FROM指令开头‌，指定基础镜像（如FROM python:3.8-slim）‌23
每行一条指令，‌指令不区分大小写‌（惯例全大写）‌25
注释以 # 开头，可单独成行或接在指令后（如RUN apt update # 更新软件源）‌35

## ‌‌指令叠加与换行‌

长指令可通过反斜杠 \ 换行（如RUN apt update && \ apt install -y curl）‌35
指令参数支持两种格式：
``` shell
RUN ["可执行文件", "参数1", "参数2"]  # JSON数组格式（需严格转义）‌:ml-citation{ref="2,5" data="citationList"}
RUN yum install -y httpd           # Shell命令格式‌:ml-citation{ref="2,5" data="citationList"}

```

# 二、核心指令详解
``` shell
FROM‌ #指定基础镜像，必须为第一条指令	
    FROM ubuntu:20.04
‌RUN‌ #执行命令（安装依赖、编译代码等）	
    RUN pip install -r requirements.txt	
‌COPY‌ #复制本地文件到镜像（不支持URL）	
    COPY app.py /app/
‌ADD‌ #类似COPY，支持URL和自动解压	
    ADD https://example.com/file.tar.gz /data/
‌WORKDIR‌ #设置工作目录（后续指令基于此路径执行）	
    WORKDIR /app
‌CMD‌ #定义容器启动时默认执行的命令（可被docker run覆盖）	
    CMD ["python", "app.py"]
‌EXPOSE‌ #声明容器监听的端口（需配合docker run -p映射）	
    EXPOSE 80
‌ENV‌ #设置环境变量（持久化到容器）	
    ENV NODE_ENV=production
```

# 三、格式优化与规范
## ‌分层构建‌
* 按依赖变更频率排序指令，利用缓存加速构建（如先COPY requirements.txt再RUN pip install）‌45
* 合并同类指令减少镜像层数（如RUN apt update && apt install -y curl）‌56

## ‌‌辅助文件‌
* 使用.dockerignore文件排除无关文件（如日志、临时文件）‌36
* 多阶段构建分离编译环境与运行环境（如FROM ... AS builder和COPY --from=builder）‌

# 完整实例
``` shell
# 基于 Ubuntu 20.04 镜像构建‌:ml-citation{ref="5" data="citationList"}
FROM ubuntu:20.04

# 设置环境变量‌:ml-citation{ref="5" data="citationList"}
ENV DEBIAN_FRONTEND=noninteractive

# 更新系统并安装依赖‌:ml-citation{ref="5,6" data="citationList"}
RUN apt update && \
    apt install -y python3-pip

# 复制代码到镜像‌:ml-citation{ref="5" data="citationList"}
COPY . /app
WORKDIR /app

# 安装 Python 依赖‌:ml-citation{ref="5" data="citationList"}
RUN pip install -r requirements.txt

# 声明端口并定义启动命令‌:ml-citation{ref="5,6" data="citationList"}
EXPOSE 80
CMD ["python3", "app.py"]

```

# 注意事项  
* 指令顺序敏感‌：频繁变更的指令（如代码复制）应放在文件后部，避免频繁重建缓存‌45
* ‌多平台兼容‌：Windows 环境下需注意路径分隔符（如COPY app C:\\app）‌6
* ‌生产优化‌：使用轻量级基础镜像（如Alpine Linux）并移除调试工具‌35