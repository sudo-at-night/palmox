from graphene import List, Field, ObjectType, Boolean, String, Int, Schema
from graphql import GraphQLError
from models.feature_flag_dao import FeatureFlagDao


class FeatureFlag(ObjectType):
    """
    A feature flag created by the user in the system.
    """

    key = String()
    name = String()
    is_active = Boolean()


class Query(ObjectType):
    feature_flag = Field(FeatureFlag, key=String())
    feature_flags = Field(List(FeatureFlag))

    def resolve_feature_flag(root, info, key: str):
        flag_dao = FeatureFlagDao()

        try:
            flag = flag_dao.get(key)
        except:
            raise GraphQLError("Internal error, cannot fetch the flag")

        return flag

    def resolve_feature_flags(root, info):
        flag_dao = FeatureFlagDao()

        try:
            flags = flag_dao.get_all()
        except:
            raise GraphQLError("Internal error, cannot fetch flags")

        return flags


schema = Schema(query=Query)
