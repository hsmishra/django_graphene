import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

import app.schema


class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   update_account = mutations.UpdateAccount.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()

class Query(app.schema.Query, UserQuery, MeQuery, graphene.ObjectType):
    pass


class Mutation(app.schema.Mutation, AuthMutation,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

