# Generated by Django 3.1.2 on 2020-10-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_news_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.URLField(default='static/img/bg.jpg'),
        ),
    ]