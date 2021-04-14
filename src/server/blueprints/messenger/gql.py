from graphene import List, Field, ObjectType, String, Schema, Boolean
from models.feature_flag_dao import FeatureFlagDao

class FeatureFlag(ObjectType):
    """
    A feature flag created by the user in the system.
    """

    id = String()
    name = String()
    is_active = Boolean()


class Query(ObjectType):
    feature_flag = Field(FeatureFlag, id=String())
    feature_flags = Field(List(FeatureFlag))

    def resolve_feature_flag(root, info, id):
        flag_dao = FeatureFlagDao()

        return flag_dao.get_by_id(id)

    def resolve_feature_flags(root, info):
        flag_dao = FeatureFlagDao()

        return flag_dao.get_all()


schema = Schema(query=Query)
