from .redis import redis_instance

def get_redis():
    return redis_instance
