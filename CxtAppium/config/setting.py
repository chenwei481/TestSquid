#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import time

now = time.strftime('%Y-%m-%d %H-%M-%S')
# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义截图的路径
IMG_PATH =  os.path.join(BASE_PATH,'results\\img')
#定义日志路径
LOG_PATH = os.path.join(BASE_PATH,'config\\log.conf')
#定义初始文件yaml路径
YAML_PATH = os.path.join(BASE_PATH,'config\\desired_caps.yaml')