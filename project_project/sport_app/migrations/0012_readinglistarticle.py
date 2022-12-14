# Generated by Django 4.1.3 on 2023-01-03 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_app', '0011_rename_exercisefavourite_favouriteexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingListArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='sport_app.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
