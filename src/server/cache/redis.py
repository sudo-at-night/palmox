from flask_caching import Cache
from dotenv import dotenv_values

config = dotenv_values(".env")

cache = Cache(config={ "CACHE_TYPE": "RedisCache", "CACHE_REDIS_HOST": "redis", "CACHE_REDIS_PASSWORD": config["REDIS_PASSWORD"] })
