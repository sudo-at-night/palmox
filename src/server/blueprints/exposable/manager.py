"""
Manager is responsible for managing the client data store,
available to clients via Redis.
"""

import json
from blinker import signal
from redis import WatchError
from events.exposable import EXPOSABLE_EVENTS
from db.redis import redis_instance as redis


def reload_data(sender, key: str, index_key: str, all_data):
    """
    Reload all Redis data for given key.
    """
    while True:
        try:
            with redis.pipeline() as pipe:
                pipe.watch(key, index_key)
                all_keys = []

                pipe.multi()
                for data in all_data:
                    data_key = data["key"]
                    all_keys.append(data_key)
                    pipe.set(f"{key}::{data_key}", json.dumps(data))

                keys_separator = " "
                pipe.delete(index_key)
                pipe.lpush(index_key, keys_separator.join(all_keys))
                pipe.execute()
                break
        except WatchError:
            continue
    


def reload_data_single(sender, key: str, index_key: str, id: str, data):
    """
    Reload Redis data for given key and given id.
    """
    json_data = json.dumps(data)

    while True:
        try:
            with redis.pipeline() as pipe:
                pipe.watch(key, index_key)
                all_keys = pipe.lrange(index_key, 0, -1)
                matching_id = next(
                    (d for d in all_keys if d.decode("utf-8") == id), None
                )
                pipe.multi()
                if not matching_id:
                    pipe.lpush(index_key, id)
                pipe.set(f"{key}::{id}", json_data)
                pipe.execute()
                break
        except WatchError:
            continue


signal(EXPOSABLE_EVENTS.MISSING_DATA_ALL).connect(reload_data)
signal(EXPOSABLE_EVENTS.MISSING_DATA_SINGLE).connect(reload_data_single)
