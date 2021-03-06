# Generated by Django 3.1.4 on 2020-12-29 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_papermodel_paper_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='article_category',
            field=models.CharField(choices=[('FinTech & Investing', 'fintech_investing'), ('Machine Learning', 'machine_learning'), ('Computational Biology', 'computational_biology'), ('Data Engineering', 'data_engineering'), ('Web Development', 'web_development')], max_length=50, null=True, verbose_name='Article Category'),
        ),
        migrations.AlterField(
            model_name='papermodel',
            name='paper_category',
            field=models.CharField(choices=[('FinTech & Investing', 'fintech_investing'), ('Machine Learning', 'machine_learning'), ('Computational Biology', 'computational_biology'), ('Data Engineering', 'data_engineering'), ('Web Development', 'web_development')], max_length=50, verbose_name='Paper Category'),
        ),
    ]
