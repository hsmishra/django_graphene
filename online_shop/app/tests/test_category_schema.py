from django.test import TestCase

from graphene.test import Client
from mixer.backend.django import mixer
import pytest

from app.models import Category

from online_shop.schema import  schema



category_list_query = """
query{
  allCategories{
    name
    id
  }
}
"""

create_category_mutation = """
     mutation createCategory(name:"Fruits"){
        category{
          id
          name
        }
      }
"""

@pytest.mark.django_db
class TestCategory(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.category = mixer.blend(Category)

    def test_category_list(self):
        mixer.blend(Category)
        response = self.client.execute(category_list_query)
        categories = response.get("data").get("allCategories")
        ok = response.get("data").get("ok")
        assert len(categories)