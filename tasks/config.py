broker_url = 'redis://192.144.186.212:6379/2'
broker_pool_limit = 10  # Borker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']
task_serializer = 'pickle'

result_backend = 'redis://192.144.186.212:6379/2'
result_serializer = 'pickle'
result_cache_max = 10000  # 任务结果最大缓存数量
result_expires = 3600  # 任务结果过期时间

worker_redirect_stdouts_level = 'INFO'
