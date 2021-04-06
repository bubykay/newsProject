import graphene
from graphene_django import DjangoObjectType
from .models import ScrapedNews


class AllNews(DjangoObjectType):
    class Meta:
        model = ScrapedNews
        fields = ("id", "source", "image", "body", "views", "title")


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(AllNews)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return ScrapedNews.objects.all()

    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Category.objects.get(name=name)
    #     except Category.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query);