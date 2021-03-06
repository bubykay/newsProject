# Generated by Django 3.1.2 on 2020-10-30 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20201028_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.CharField(default='static/img/bg.jpg', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='keywords',
            field=models.CharField(default='NA', max_length=500),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
