import os
import sys

import django

print(__file__)  #当前文件的路径（绝对路径和相对路径都有可能）
print(os.path.abspath(__file__))  #展示当前路径的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  #dirname文件夹的名字，这行命令表示当前文件的文件夹名字
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 第一步：将项目的绝对路径加载到 sys.path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# 第二步：设置环境变量 DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

# 第三步：Django 环境初始化
django.setup()

from user.models import User
