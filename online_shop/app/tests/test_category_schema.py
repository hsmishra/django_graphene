from django.test import TestCase

import pytest
from graphene.test import Client
from mixer.backend.django import mixer

from app.models import Category
from app.tests.schema_format import (category_list_query,
                                     create_category_mutation,
                                     single_category_query,
                                     update_category_mutation)
from online_shop.schema import schema


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
        payload = {"id": self.category.id, "name": "car"}
        response = self.client.execute(update_category_mutation, variables=payload)
        response_cat = response.get("data").get("updateCategory").get("category")
        name = response_cat.get("name")
        assert name == payload["name"]
        assert name != self.category.name

    # ======================= Test create category mutation=======================
    # def test_delete_category(self):
    #     payload = {"id": self.category.id}
    #     response = self.client.execute(delete_category_mutation, variables=payload)
    #     delete_res = response.get("data").get("deleteCategory").get("category")
    #     id = delete_res.get("id")
    #     assert id == None
