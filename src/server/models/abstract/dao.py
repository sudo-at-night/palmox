import json
from typing import Dict, Union, Generic, TypeVar, List, Union
from abc import ABCMeta, abstractmethod
from redis import WatchError
from blinker import signal
from events.exposable import EXPOSABLE_EVENTS
from db.redis import redis_instance as redis

R = TypeVar("R")
P = TypeVar("P")


class AbstractExposableDao(Generic[R, P], metaclass=ABCMeta):
    """
    Exposable data is exposed to system's clients
    via Redis model.

    If exposable data is not available in Redis, it should
    be retrieved from system's main database.
    """

    REDIS_INDEX_KEY: str
    """ In Redis, this leads to where a given data's array of available indexes is. """
    REDIS_KEY: str
    """ In Redis, this leads to where the given data is stored """

    def get(self, id: str) -> Union[R, None]:
        """
        Retrieve a representation of given data type.
        """
        RedisClass = self._get_extended_redis_class()
        PostgresClass = self._get_extended_postgres_class()

        redis_data = redis.get(f"{self.REDIS_KEY}::{id}")
        if not redis_data:
            postgres_data = PostgresClass.query.filter_by(key=id).first()
            if not postgres_data:
                return None

            parsed_model = self._parse_postgres_to_dict(postgres_data)
            signal(EXPOSABLE_EVENTS.MISSING_DATA_SINGLE).send(self, key=self.REDIS_KEY, index_key=self.REDIS_INDEX_KEY, id=id, data=parsed_model)
            return RedisClass(**parsed_model)

        return RedisClass(**self._parse_redis_to_dict(redis_data))

    def get_all(self) -> List[R]:
        """
        Retrieve all representations of given data type.
        """
        RedisClass = self._get_extended_redis_class()
        PostgresClass = self._get_extended_postgres_class()

        all_data = []
        raw_all_data = []
        redis_data = self._get_all_from_redis()

        if redis_data:
            for data in redis_data:
                all_data.append(RedisClass(**self._parse_redis_to_dict(data)))
        else:
            postgres_data = PostgresClass.query.all()
            for data in postgres_data:
                all_data.append(
                    RedisClass(**self._parse_postgres_to_dict(data))
                )
                raw_all_data.append(self._parse_postgres_to_dict(data))
            if all_data:
                signal(EXPOSABLE_EVENTS.MISSING_DATA_ALL).send(self, key=self.REDIS_KEY, index_key=self.REDIS_INDEX_KEY, all_data=raw_all_data)

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
                        specific_data = pipe.get(f"{self.REDIS_KEY}::{key}")
                        if specific_data:
                            all_data.append(specific_data)
                    break
                except WatchError:
                    all_data = []
                    continue

        return all_data

    def _get_extended_redis_class(self):
        return self.__orig_bases__[0].__args__[0]

    def _get_extended_postgres_class(self):
        return self.__orig_bases__[0].__args__[1]

    @classmethod
    def _parse_redis_to_dict(cls, redis_field) -> Dict[str, str]:
        """
        Parses Redis JSON field to a Python dictionary.
        """
        return json.loads(redis_field)

    @abstractmethod
    def _parse_postgres_to_dict(self, postgres_class: P) -> Dict[str, str]:
        """
        Parses Postgres model of given type to a Python dictionary.

        This needs to be implemented on every extending class
        to understand how to map internal Postgres database schema
        to an exposable Redis data model.
        """
        pass
