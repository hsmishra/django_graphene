import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

from app.schemas import category_schema, product_schema


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()


class Query(product_schema.Query, category_schema.Query, UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(product_schema.Mutation, category_schema.Mutation, AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
