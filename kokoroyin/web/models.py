from django.db import models

# Create your models here.


class ScrapedNews(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=500, unique=True)
    body = models.TextField()
    img = models.CharField(max_length=300, default='static/img/bg.jpg', null=True)
    keywords = models.CharField(max_length=500, default='NA')
    views = models.IntegerField(default=0)
    source = models.CharField(max_length=300, default='kokoroyin')
    image = models.URLField(null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
