import graphene
from graphql_auth.schema import UserQuery, MeQuery

import app.schema

class Query(app.schema.Query, UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(app.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

