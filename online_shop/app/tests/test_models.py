import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestProductModel:

    def test_product_is_in_stock(self):
        product = mixer.blend('app.Product', in_stock=True)
        assert product.is_in_stock == True
    
    def test_product_is_not_in_stock(self):
        product = mixer.blend('app.Product', in_stock=False)
        assert product.is_in_stock == False