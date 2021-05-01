from .abstract.dao import AbstractExposableDao
from .project import Project


class ProjectDao(AbstractExposableDao[Project]):
    CACHE_PREFIX = "project"

    def _parse_model_to_client_model(self, original_model: Project):
        return {
            "key": original_model.key,
            "name": original_model.name,
            "feature_flags": original_model.feature_flags,
        }