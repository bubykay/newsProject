from django.urls import path
from . import views
from graphene_django.views import GraphQLView


urlpatterns = [
    path(r'', views.index, name='home'),
    path(r'<slug:slug>/', views.news, name='news'),
    path(r'graphql', GraphQLView.as_view(graphiql=True)),
]
