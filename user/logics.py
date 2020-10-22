import re
import random
import logging

from libs.cache import rds
from libs.sms import send_sms
from common import keys
from tasks import celery_app

inf_log = logging.getLogger('inf')


def is_phonenum(phonenum):
    '''验证是否是一个正确的手机号'''
    if re.match(r'1[3-9]\d{9}$', phonenum):
        return True
    else:
        return False


def random_code(length=6):
    '''产生指定长度随机码'''
    nums = [str(random.randint(0, 9)) for i in range(length)]
    return ''.join(nums)

@celery_app.task
def send_vcode(phonenum):
    '''给用户发送短信验证码'''
    # 验证手机号
    if not is_phonenum(phonenum):
        return False

    key = keys.VCODE_K % phonenum

    # 检查缓存中是否已有验证码，防止用户频繁调用接口
    if rds.get(key):
        return True

    # 产生验证码
    vcode = random_code()
    inf_log.debug(f'验证码：{phonenum}-{vcode}')
    rds.set(key, vcode, 600)  # 将验证码添加到缓存，并多设置一些时间

    return send_sms(phonenum, vcode)  # 向用户手机发送验证码

