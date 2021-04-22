from .abstract.dao import AbstractExposableDao
from .project import RedisProject, PostgresProject


class ProjectDao(AbstractExposableDao[RedisProject, PostgresProject]):
    REDIS_INDEX_KEY = "projects"
    REDIS_KEY = "project"
    POSTGRES_FILTER_COLUMN = "key"

    def _parse_postgres_to_dict(self, postgres_class: PostgresProject):
        return {
            "key": postgres_class.key,
            "name": postgres_class.name,
            "feature_flags": postgres_class.feature_flags,
        }