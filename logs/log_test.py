import logging
from logging import handlers

# 设置日志格式
fmt = '%(asctime)s %(levelname)7.7s %(funcName)s: %(message)s'
formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

# 设置 handler
handler = handlers.TimedRotatingFileHandler('myapp.logs', when='midnight', backupCount=3)
handler.setFormatter(formatter)

# 定义 logger 对象
logger = logging.getLogger("MyApp")
logger.addHandler(handler)
logger.setLevel(logging.INFO)
