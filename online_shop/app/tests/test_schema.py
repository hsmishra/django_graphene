from graphene.test import Client

from online_shop.schema import  schema

def test_hey(snapshot):
    print("")
    client = Client(schema)
    snapshot.assert_match(client.execute('''{ hey }'''))