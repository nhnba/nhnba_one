from django.db import models

# Create your models here.

class User(models.Model):
	'''User模型'''
	GENDERS = (
		('male','男'),
		('female','女'),
	)
	LOCATIONS = (
		('北京', '北京'),
		('上海', '上海'),
		('深圳', '深圳'),
		('成都', '成都'),
		('西安', '西安'),
		("武汉", "武汉"),
		("沈阳", "沈阳")
	)

	phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
	nickname = models.CharField(max_length=20, db_index=True, verbose_name='昵称')
	gender = models.CharField(max_length=10, choices=GENDERS, default='male',verbose_name='性别')
	birthday = models.DateField(default='2002-01-01', verbose_name='出生日')
	avatar = models.CharField(max_length=256, verbose_name='个人形象')
	location = models.CharField(max_length=10, choices=LOCATIONS,default='上海', verbose_name='常居地')

	@property
	def profile(self):
		'''当前用户对应的profile'''
		if not hasattr(self,'_profile'):
			self._profile,_=Profile.objects.get_or_create(id=self.id)
		return self._profile

	def to_dict(self):
		return {
			'id': self.id,
			'phonenum': self.phonenum,
			'nickname': self.nickname,
			'gender': self.gender,
			'birthday': str(self.birthday),
			'avatar': self.avatar,
			'location': self.location,
		}

class Profile(models.Model):
	'''用户的交友资料'''
	dating_location = models.CharField(max_length=10,default='上海',choices=User.LOCATIONS,verbose_name='⽬标城市')
	dating_gender = models.CharField(max_length=10,default='female',choices=User.GENDERS,verbose_name='匹配的性别')
	min_distance = models.IntegerField(default=1,verbose_name='最⼩查找范围')
	max_distance = models.IntegerField(default=50,verbose_name='最⼤查找范围')
	min_dating_age = models.IntegerField(default=18,verbose_name='最⼩交友年龄')
	max_dating_age = models.IntegerField(default=50,verbose_name='最⼤交友年龄')
	vibration = models.BooleanField(default=True,verbose_name='开启震动')
	only_matched = models.BooleanField(default=True,verbose_name='不让陌⽣⼈看我的相册')
	auto_play  = models.BooleanField(default=True,verbose_name='⾃动播放视频')

	def to_dict(self):
		return {
			'id':self.id,
			'dating_location':self.dating_location,
			'dating_gender':self.dating_gender,
			'min_distance':self.min_distance,
			'max_distance':self.max_distance,
			'min_dating_age':self.min_dating_age,
			'max_dating_age':self.max_dating_age,
			'vibration':self.vibration,
			'only_matched':self.only_matched,
			'auto_play':self.auto_play,
		}