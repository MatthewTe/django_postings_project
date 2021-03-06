# Generated by Django 3.1.4 on 2020-12-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, verbose_name='Article Titile')),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('article_description', models.CharField(max_length=200, verbose_name='Article Description')),
                ('articel_content', models.FileField(upload_to='articles/', verbose_name='Article Content Markdown File')),
                ('article_slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('article_category', models.CharField(choices=[('FinTech & Investing', 'fintech_investing'), ('Machine Learning', 'machine_learning'), ('Computational Biology', 'computational_biology'), ('Data Engineering', 'data_engineering')], max_length=50, null=True, verbose_name='Article Category')),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'ordering': ['-upload_date'],
            },
        ),
    ]
