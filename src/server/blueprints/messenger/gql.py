from graphene import List, Field, ObjectType, String, Schema, Boolean

class FeatureFlag(ObjectType):
    """
    A feature flag created by the user in the system.
    """

    id = String()
    is_on = Boolean()


class Query(ObjectType):
    feature_flag = Field(FeatureFlag, id=String())
    feature_flags = Field(List(FeatureFlag))

    def resolve_feature_flag(root, info, id):
        return {
            "id": id,
            "is_on": "AFK Flag",
        }


schema = Schema(query=Query)
