# Generated by Django 3.1.2 on 2020-10-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201028_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
