# Generated by Django 4.1.3 on 2023-01-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_rating_comment_alter_rating_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
