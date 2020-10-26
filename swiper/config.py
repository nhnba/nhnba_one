'''程序逻辑配置，及第三方平台配置'''

#redis配置
REDIS={
	'host':'localhost',
	'port':6379,
	'db':2,
}

#滑动积分
# 滑动积分
SWIPE_SCORE = {
    'like': 5,
    'superlike': 7,
    'dislike': -5
}

# 排行榜数量
RANK_NUM = 50

# 赛迪云通信设置
SD_APPID = '54732'
SD_APPKEY = '86cf99e7eda5c6d3d8635a0d5fea118a'
SD_PROJECT = 'qAbWx3'  # 短信模板的 ID
SD_SIGN_TYPE = 'md5'
SD_API = 'https://api.mysubmail.com/message/xsend.json'

#七牛云的配置
QN_DOMAIN = 'qh5yz3mtt.hd-bkt.clouddn.com'
QN_BUCKET = 'nhnba'
QN_ACCESS_KEY = 'dwSaTakKQHyofIn3TnvZVVzOvczTuaupUCM9sx-e'
QN_SECRET_KEY = 'ZNmqN_Wzpi-zyccejwdnPR2j94XeDOh76-PH1gf-'
QN_CALLBACK_URL = 'http://192.144.186.212:9000/qiniu/callback'
QN_CALLBACK_DOMAIN = '192.144.186.212'

# 反悔功能相关配置
REWIND_TIMES = 3         # 每日反悔次数
REWIND_TIMEOUT = 5 * 60  # 反悔超时时间