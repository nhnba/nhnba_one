#!/bin/bash
# 项目启动脚本

PROJECT_DIR='/opt/swiper'

cd $PROJECT_DIR
source ./venv/bin/activate
gunicorn -c swiper/gconfig.py swiper.wsgi
deactivate

echo '程序启动成功'