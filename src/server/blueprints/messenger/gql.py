import random
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String()

    def resolve_hello(root, info, name):
        return f"Hello!"

schema = Schema(query=Query)
