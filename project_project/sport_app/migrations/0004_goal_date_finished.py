# Generated by Django 4.1.3 on 2023-01-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0003_article_slug_exercise_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='date_finished',
            field=models.DateTimeField(default='1900-12-12'),
            preserve_default=False,
        ),
    ]
