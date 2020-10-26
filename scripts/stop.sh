#!/bin/bash
# 停止脚本

PROJECT_DIR='/opt/swiper'
PID_FILE="$PROJECT_DIR/logs/gunicorn.pid"

if [ -f $PID_FILE ]; then
    PID=`cat $PID_FILE`
    kill $PID
    echo '程序已终止'
else
    echo '程序尚未启动'
fi
