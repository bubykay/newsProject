"""kokoroyin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from web.sitemap import Static_Sitemap, Article_Sitemap
from graphene_django.views import GraphQLView

sitemaps = {
    'static': Static_Sitemap,
    'article': Article_Sitemap
}

web_url = include('web.urls')
urlpatterns = [
    path('slug:slug', web_url),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('admin/', admin.site.urls),
    path('', web_url),
    path(r'^graphql$', GraphQLView.as_view(graphiql=True)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

