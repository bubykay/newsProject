# Generated by Django 3.1.2 on 2020-10-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_news_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='source',
            field=models.CharField(default='kokoroyin', max_length=300),
        ),
    ]
