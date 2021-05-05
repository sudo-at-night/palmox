import json
from exceptions import IncorrectImplementingClass
from typing import Dict, Union, Generic, TypeVar, Union
from abc import ABCMeta, abstractmethod
from cache.redis import cache

T = TypeVar("T")


class AbstractExposableDao(Generic[T], metaclass=ABCMeta):
    """
    Exposable data is exposed to system's clients
    via separate model.
    """

    CACHE_PREFIX: str
    """ Unique resource cache key prefix """

    def __init__(self):
        ExtendedClass = self._get_extended_class()

        if (
            not hasattr(ExtendedClass, "query")
            or not hasattr(ExtendedClass.query, "filter_by")
            or not hasattr(ExtendedClass.query, "all")
        ):
            raise IncorrectImplementingClass(
                implementing_class=self,
                reason="Implementing class has to use a class derived from SQLAlchemy model which can be queried",
            )

    def get(self, id: str):
        """
        Retrieve a representation of given data type.
        """
        ExtendedClass = self._get_extended_class()
        resource_cache_key = f"{self.CACHE_PREFIX}::{id}"

        cached_result = cache.get(resource_cache_key)
        if cached_result:
            return cached_result

        data = ExtendedClass.query.filter_by(key=id).first()

        if data:
            parsed_response = self._parse_model_to_client_model(data)
            cache.set(resource_cache_key, parsed_response)
            return parsed_response

        return None

    def get_all(self):
        """
        Retrieve all representations of given data type.
        """
        ExtendedClass = self._get_extended_class()
        resource_cache_key = f"{self.CACHE_PREFIX}::"

        cached_result = cache.get(resource_cache_key)
        if cached_result:
            return cached_result

        all_data = []

        data = ExtendedClass.query.all()
        for data in data:
            all_data.append(self._parse_model_to_client_model(data))

        cache.set(resource_cache_key, all_data)
        return all_data

    def _get_extended_class(self):
        return self.__orig_bases__[0].__args__[0]

    @abstractmethod
    def _parse_model_to_client_model(self, original_model: T):
        """
        Parses retreived model of given type to a Python dictionary.

        This needs to be implemented on every extending class
        to understand how to map internal database model
        to an exposable client data model.
        """
        pass
