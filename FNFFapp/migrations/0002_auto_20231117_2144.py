# Generated by Django 3.2.23 on 2023-11-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FNFFapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
