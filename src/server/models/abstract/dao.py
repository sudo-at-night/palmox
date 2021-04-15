from typing import Dict, Union, Generic, TypeVar, List, Union
from abc import ABCMeta, abstractmethod
from redis import WatchError
from db.redis import redis_instance as redis

T = TypeVar("T")


class AbstractExposableDao(Generic[T], metaclass=ABCMeta):
    """
    Exposable data is exposed to system's clients
    via Redis model.

    If exposable data is not available in Redis, it should
    be retrieved from system's main database, at the same
    time system's "web" blueprint should be informed about
    a missing data instance. "Web" blueprint be responsible
    for updating the Redis database.
    """

    REDIS_INDEX_KEY: str
    """ In Redis, this leads to where a given data's array of available indexes is. """
    REDIS_KEY: str
    """ In Redis, this leads to where the given data is stored """

    def get_by_id(self, id: Union[str, int]) -> Union[T, None]:
        """
        Retrieve a representation of given data type.
        """
        RedisClass = self._get_extended_redis_class()
        redis_data = redis.hgetall(f"{self.REDIS_KEY}::{id}")
        if not bool(redis_data):
            return None

        return RedisClass(**self._parse_hash_to_dict(redis_data))

    def get_all(self) -> List[T]:
        """
        Retrieve all representations of given data type.
        """
        RedisClass = self._get_extended_redis_class()
        all_data = []
        redis_data = self._get_all_from_redis()

        for data in redis_data:
            all_data.append(RedisClass(**self._parse_hash_to_dict(data)))

        return all_data

    def _get_all_from_redis(self):
        """
        Fetch all data from Redis, based on REDIS_KEY_INDEX
        in a single transaction.

        REDIS_KEY_INDEX has the following structure and is simply
        an array of all available data keys of a given type:
        <REDIS_INDEX_KEY> contains <KEY> for
          <REDIS_KEY>::<KEY>
        """
        with redis.pipeline() as pipe:
            all_data = []

            while True:
                try:
                    pipe.watch(self.REDIS_INDEX_KEY)
                    all_keys = pipe.lrange(self.REDIS_INDEX_KEY, 0, -1)
                    for byte_key in all_keys:
                        key = byte_key.decode("utf-8")
                        specific_data = pipe.hgetall(f"{self.REDIS_KEY}::{key}")
                        if bool(specific_data):
                            all_data.append(specific_data)
                    break
                except WatchError:
                    all_data = []
                    continue

        return all_data

    def _get_extended_redis_class(self):
        return self.__orig_bases__[0].__args__[0]

    @classmethod
    def _parse_hash_to_dict(cls, redis_hash) -> Dict[str, str]:
        new_dict = {}
        for key, value in redis_hash.items():
            new_dict[key.decode("utf-8")] = value.decode("utf-8")

        return new_dict
