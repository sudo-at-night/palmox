from .abstract.dao import AbstractExposableDao
from .feature_flag import RedisFeatureFlag


class FeatureFlagDao(AbstractExposableDao[RedisFeatureFlag]):
    REDIS_INDEX_KEY = "feature-flags"
    REDIS_KEY = "feature-flag"
