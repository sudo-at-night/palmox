import redis
from dotenv import dotenv_values

config = dotenv_values(".env")

redis_instance = redis.Redis(host="db_messenger", port=6379, db=0, password=config["REDIS_PASSWORD"])
