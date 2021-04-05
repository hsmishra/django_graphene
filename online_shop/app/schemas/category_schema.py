import graphene
from graphene import Argument
from graphene_django.types import DjangoObjectType

from ..models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(object):
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.ID())

    def resolve_all_categories(self, info, **kwargs):
        # Querying a list of categories
        return Category.objects.all()

    def resolve_category(self, info, id):
        # Querying a single category
        return Category.objects.get(pk=id)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name):
        category = Category.objects.create(
            name=name
        )
        return CreateCategory(
            category=category
        )


class UpdateCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name):
        category = Category.objects.get(pk=id)
        category.name = name if name is not None else category.name
        category.save()
        return UpdateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id):
        category = Category.objects.get(pk=id)
        if category is not None:
            category.delete()
        return DeleteCategory(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
