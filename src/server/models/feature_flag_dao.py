from .abstract.dao import AbstractExposableDao
from .feature_flag import FeatureFlag


class FeatureFlagDao(AbstractExposableDao[FeatureFlag]):
    CACHE_PREFIX = "feature-flag"

    def _parse_result_to_dict(self, original_model: FeatureFlag):
        return {
            "key": original_model.key,
            "name": original_model.name,
            "is_active": original_model.is_active,
        }
