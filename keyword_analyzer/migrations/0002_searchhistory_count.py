# Generated by Django 3.2 on 2022-02-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyword_analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
