from db import get_redis
from .abstract.dao import AbstractExposableDao
from .feature_flag import FeatureFlag


class FeatureFlagDao(AbstractExposableDao[FeatureFlag]):
    REDIS_INDEX_KEY = "feature-flags"
    REDIS_KEY = "feature-flag"

    def get_by_id(self, id) -> FeatureFlag:
        """
        Retrieve a feature flag from the system.
        """
        flag = get_redis().hgetall(f"{self.REDIS_KEY}::{id}")

        return FeatureFlag(**self._parse_hash_to_dict(flag))

    def get_all(self):
        """
        Retrieve all feature flags from the system.
        """
        all_flags = []
        flags_data = self._get_all_from_redis()

        for flag in flags_data:
            all_flags.append(FeatureFlag(**self._parse_hash_to_dict(flag)))

        return all_flags
