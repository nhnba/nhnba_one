#写注释啊，别打错别字啊
from redis import Redis as _Redis
import pickle
from pickle import UnpicklingError
from swiper.config import REDIS

class Redis(_Redis):
	def set(self,name,value,ex=None,px=None,nx=False,xx=False):
		'''带序列化处理的 set 方法'''
		pickled_data = pickle.dumps(value, pickle.HIGHEST_PROTOCOL)
		return super().set(name, pickled_data, ex, px, nx, xx)

	def get(self, name, default=None):
		'''带序列化处理的 get 方法'''
		pickled_data = super().get(name)

		if pickled_data is None:
			return default

		try:
			value = pickle.loads(pickled_data)
		except (KeyError, EOFError, UnpicklingError):
			return pickled_data
		else:
			return value

rds = Redis(**REDIS)