# Generated by Django 4.1.3 on 2022-12-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
