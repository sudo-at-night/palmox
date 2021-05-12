from graphene import List, Field, ObjectType, Boolean, String, Schema
from graphql import GraphQLError
from models.feature_flag_dao import FeatureFlagDao
from models.project_dao import ProjectDao


class FeatureFlag(ObjectType):
    key = String()
    name = String()
    is_active = Boolean()


class Project(ObjectType):
    key = String()
    name = String()
    feature_flags = List(FeatureFlag)


class Query(ObjectType):
    feature_flag = Field(FeatureFlag, key=String())
    feature_flags = Field(List(FeatureFlag))
    project = Field(Project, key=String())
    projects = Field(List(Project))

    def resolve_feature_flag(root, info, key: str):
        flag_dao = FeatureFlagDao()

        try:
            flag = flag_dao.get(key)
        except Exception:
            raise GraphQLError("Internal error, cannot fetch the flag")

        return flag

    def resolve_feature_flags(root, info):
        flag_dao = FeatureFlagDao()

        try:
            flags = flag_dao.get_all()
        except Exception:
            raise GraphQLError("Internal error, cannot fetch flags")

        return flags

    def resolve_project(root, info, key):
        project_dao = ProjectDao()

        try:
            project = project_dao.get(key)
        except Exception:
            raise GraphQLError("Internal error, cannot fetch the project")

        return project

    def resolve_projects(root, info):
        project_dao = ProjectDao()

        try:
            project = project_dao.get_all()
        except Exception:
            raise GraphQLError("Internal error, cannot fetch projects")

        return project


schema = Schema(query=Query)
