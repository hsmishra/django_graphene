import pytest
from django.test import TestCase
from graphene.test import Client
from mixer.backend.django import mixer
from online_shop.schema import schema

from app.models import Category

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

update_category_mutation = """
    mutation updateCategory($name: String, $id: ID){
        updateCategory(name: $name, id: $id)
        {
            category{
                name
                id
            }
        }
    }
"""

@pytest.mark.django_db
class TestCategory(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.category = mixer.blend(Category)

    # ======================= Test all categories=======================
    def test_category_list(self):
        mixer.blend(Category)
        response = self.client.execute(category_list_query)
        categories = response.get("data").get("allCategories")
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
        payload = {"name": "lap"}
        response = self.client.execute(create_category_mutation, variables=payload)
        category = response.get("data").get("createCategory").get("category")
        name = category.get("name")
        assert name == "lap"

    # ======================= Test create category mutation=======================
    def test_update_category(self):
        # breakpoint()
        payload = {"id": self.category.id, "name": "car"}
        response = self.client.execute(update_category_mutation, variables=payload)

        response_cat = response.get("data").get("updateCategory").get("category")
        name = response_cat.get("name")
        assert name == payload["name"]
        assert name != self.category.name
