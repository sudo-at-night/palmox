from graphene import List, Field, ObjectType, String, Schema, Boolean
from graphql import GraphQLError
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

        try:
            flag = flag_dao.get_by_id(id)
        except:
            raise GraphQLError("Error when fetching the flag")

        return flag

    def resolve_feature_flags(root, info):
        flag_dao = FeatureFlagDao()

        try:
            flags = flag_dao.get_all()
        except:
            raise GraphQLError("Error when fetching flags")

        return flags


schema = Schema(query=Query)
