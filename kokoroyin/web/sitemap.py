from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ScrapedNews

class Static_Sitemap(Sitemap):

    # priority = 1.0
    # changefreq = 'hourly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class Article_Sitemap(Sitemap):
    # changefreq = "hourly"
    # priority = 0.7

    def items(self):
        return ScrapedNews.objects.all().order_by('-pk')

    # def location(self, obj):
    #     return obj.note_full_path

    # def lastmod(self, obj): 
    #     return obj.created