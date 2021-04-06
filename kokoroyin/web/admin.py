from django.contrib import admin
from .models import ScrapedNews

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    model = ScrapedNews
    list_display = ['source','title', 'img','slug']
    # list_editable = ['source','title', 'img', 'slug']

admin.site.register(ScrapedNews, NewsAdmin)
