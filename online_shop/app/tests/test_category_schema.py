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

single_category_query = """

    query{
      category(id: 1) {
        id
        name
      }
    }

"""

create_category_mutation = """
     mutation createCategory($name: String) {
        createCategory(name: $name){
            category{
                name
            }
        }
  }

"""

@pytest.mark.django_db
class TestCategory(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.category = mixer.blend(Category)

    #======================= Test all categories=======================
    def test_category_list(self):
        mixer.blend(Category)
        response = self.client.execute(category_list_query)
        categories = response.get("data").get("allCategories")
        ok = response.get("data").get("ok")
        assert len(categories)

    # ======================= Test single category=======================
    def test_single_category(self):
        mixer.blend(Category)
        response = self.client.execute(single_category_query)
        category = response.get("data").get("category")
        id = category.get("id")
        assert id == id

    # ======================= Test create category mutation=======================
    def test_create_category(self):
        payload = {"name":"lap"}
        response = self.client.execute(create_category_mutation, variables=payload)
        category = response.get("data").get("createCategory").get("category")
        name = category.get("name")
        assert name == "lap"