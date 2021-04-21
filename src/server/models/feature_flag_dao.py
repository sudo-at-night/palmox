from .abstract.dao import AbstractExposableDao
from .feature_flag import RedisFeatureFlag, PostgresFeatureFlag


class FeatureFlagDao(AbstractExposableDao[RedisFeatureFlag, PostgresFeatureFlag]):
    REDIS_INDEX_KEY = "feature-flags"
    REDIS_KEY = "feature-flag"
    POSTGRES_FILTER_COLUMN = "key"

    def _parse_postgres_to_dict(self, postgres_class: PostgresFeatureFlag):
        return {
            "key": postgres_class.key,
            "name": postgres_class.name,
            "is_active": postgres_class.is_active,
        }
