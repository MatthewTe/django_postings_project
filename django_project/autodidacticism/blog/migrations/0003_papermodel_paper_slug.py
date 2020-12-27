# Generated by Django 3.1.4 on 2020-12-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_papermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='papermodel',
            name='paper_slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]