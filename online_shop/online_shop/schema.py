import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

import app.schema


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()

class Query(app.schema.Query, UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(app.schema.Mutation, AuthMutation,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

