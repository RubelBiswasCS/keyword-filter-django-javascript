# Generated by Django 3.2 on 2022-02-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyword_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='search_history',
        ),
        migrations.AddField(
            model_name='keyword',
            name='search_history',
            field=models.ManyToManyField(to='keyword_analyzer.SearchHistory'),
        ),
    ]
