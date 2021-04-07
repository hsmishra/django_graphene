import pytest


@pytest.fixture
def graphql_client():
    from online_shop.schema import schema
    from graphene.test import Client
    return Client(schema)
