# Generated by Django 4.1.3 on 2023-01-03 19:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_app', '0012_readinglistarticle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReadingListArticle',
            new_name='UserReadingList',
        ),
    ]
