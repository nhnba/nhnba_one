from libs.http import render_json
from libs.cache import rds
from user.logics import send_vcode
from user.models import User,Profile
from user.forms import UserForm,ProfileForm
from libs.qn_cloud import gen_token, get_res_url
from common import errors,keys

from celery import Celery, platforms

platforms.C_FORCE_ROOT = True  #加上这一行,celery才能运行起来

def fetch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    send_vcode.delay(phonenum)  #异步发送
    return render_json()


def submit_vcode(request):
    '''提交验证码，执行登录注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = keys.VCODE_K % phonenum
    cached_vcode = rds.get(key)

    if True:
    # if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)  # 从数据库获取用户
        except User.DoesNotExist:
            # 如果用户不存在，则执行注册流程
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)

        # 在 Session 中记录用户登录的状态
        request.session['uid'] = user.id

        return render_json(user.to_dict())
    else:
        return render_json(data= '验证码错误',code=errors.PROFILE_ERR)

def show_profile(request):
    '''查看个人资料'''
    uid = request.session['uid']
    profile,_ = Profile.objects.get_or_create(id=uid)
    profile.to_dict()
    return render_json(profile.to_dict())

def update_profile(request):
    '''更新个人资料'''
    #定义form对象
    user_form = UserForm(request.POST)
    profile_form = ProfileForm(request.POST)

    #检查验证数据
    if user_form.is_valid() and profile_form.is_valid():
        uid =request.session['uid']

        User.objects.filter(id=uid).update(**user_form.cleaned_data)
        Profile.objects.update_or_create(id=uid,defaults=profile_form.cleaned_data)

        return render_json()
    else:
        err = {}
        err.update(user_form.errors)
        err.update(profile_form.errors)
        return render_json(code=errors.PROFILE_ERR,data=err)

def qn_token(request):
    '''获取七牛云 Token'''
    #图片--》客户端--》服务器--》七牛云
    uid = request.session['uid']
    filename = f'Avatar-[uid]'
    token = gen_token(uid,filename)
    return render_json({
            'token':token,
            'key':filename,
    })


def qn_callback(request):
    '''七牛云回调接口'''
    uid = request.POST.get('uid')
    key = request.POST.get('key')
    avatar_url = get_res_url(key)
    User.objects.filter(id=uid).update(avatar=avatar_url)
    return render_json(avatar_url)

