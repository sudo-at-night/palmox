from .abstract.dao import AbstractExposableDao
from .feature_flag import RedisFeatureFlag, PostgresFeatureFlag


class FeatureFlagDao(AbstractExposableDao[RedisFeatureFlag, PostgresFeatureFlag]):
    REDIS_INDEX_KEY = "feature-flags"
    REDIS_KEY = "feature-flag"
