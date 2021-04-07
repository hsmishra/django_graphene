from django.test import TestCase

import pytest
from graphene.test import Client
from mixer.backend.django import mixer

from app.models import Product
from app.tests.schema_format import (product_query_list, )
from online_shop.schema import schema


@pytest.mark.django_db
class TestProduct(TestCase):
    def setUp(self):
        self.client = Client(schema)
        self.product = mixer.blend(Product)

    # ======================= Test all categories=======================
    def test_product_list(self):
        breakpoint()
        mixer.blend(Product)
        response = self.client.execute(product_query_list)
        products = response.get("data").get("allProducts")
        assert len(products)
