# -*- coding: utf-8 -*-

import logging

# 定义一个过滤器类
class MyFilter(logging.Filter):
    def filter(self, record):
        # 如果记录器名称不是 'bhlog'，则返回 False，不记录该日志
        return record.name == 'bhlog'

# 创建日志记录器
logger = logging.getLogger('bhlog')
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器
file_handler = logging.FileHandler('bhlog.log',encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# 创建一个格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加格式化器到处理器
file_handler.setFormatter(formatter)

# 添加过滤器到处理器
file_handler.addFilter(MyFilter())

# 添加处理器到日志记录器
logger.addHandler(file_handler)

#logger.info('这是一条信息级别的日志，会被记录')  # 会被记录
#another_logger = logging.getLogger('another_logger')
#another_logger.info('这是一条来自另一个模块的信息级别的日志，不会被记录')  # 不会被记录
