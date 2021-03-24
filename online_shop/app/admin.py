from django.contrib import admin
from django.apps import apps

from .models import Category, Product, CustomeUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'in_stock', 'date_created', 'get_category']

admin.site.register(CustomeUser)

app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)
