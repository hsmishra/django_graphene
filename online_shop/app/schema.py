import graphene
from graphene import Argument
from graphene_django.types import DjangoObjectType

from .models import Product, Category


class ProductType(DjangoObjectType):
  class Meta:
    model = Product


class Query(object):
  all_products = graphene.List(ProductType)
  product = graphene.Field(ProductType, id=graphene.ID())


  def resolve_all_products(self, info, **kwargs):
    # Querying a list of products
    return Product.objects.all()

  def resolve_product(self, info, id):
    # Querying a single product
    return Product.objects.get(pk=id)



class CreateProduct(graphene.Mutation):
  class Arguments:
    name = graphene.String()
    price = graphene.Float()
    category = graphene.List(graphene.ID)
    in_stock = graphene.Boolean()
    date_created = graphene.types.datetime.DateTime()

  product = graphene.Field(ProductType)

 
  def mutate(self, info, name, price=None, category=None, in_stock=True, date_created=None):
    product = Product.objects.create(
      name = name,
      price = price,
      in_stock = in_stock,
      date_created = date_created
    )

    if category is not None:
      category_set = []
      for category_id in category:
        category_object = Category.objects.get(pk=category_id)
        category_set.append(category_object)
      product.category.set(category_set)

    product.save()
    return CreateProduct(
      product=product
    )

class UpdateProduct(graphene.Mutation):
  class Arguments:
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Float()
    category = graphene.List(graphene.ID)
    in_stock = graphene.Boolean()
    date_created = graphene.types.datetime.DateTime()

  product = graphene.Field(ProductType)

  def mutate(self, info, id, name=None, price=None, category=None, in_stock=None, date_created=None):
    product = Product.objects.get(pk=id)
    product.name = name if name is not None else product.name
    product.price = price if price is not None else product.price
    product.in_stock = in_stock if in_stock is not None else product.in_stock
    product.date_created = date_created if date_created is not None else product.date_created

    if category is not None:
      category_set = []
      for category_id in category:
        category_object = Category.objects.get(pk=category_id)
        category_set.append(category_object)
      product.category.set(category_set)

    product.save()
    return UpdateProduct(product=product)


class DeleteProduct(graphene.Mutation):
  class Arguments:
    id = graphene.ID()

  product = graphene.Field(ProductType)

  def mutate(self, info, id):
    product = Product.objects.get(pk=id)
    if product is not None:
      product.delete()
    return DeleteProduct(product=product)



class Mutation(graphene.ObjectType):
  create_product = CreateProduct.Field()
  update_product = UpdateProduct.Field()
  delete_product = DeleteProduct.Field()
