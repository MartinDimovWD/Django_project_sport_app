# Generated by Django 4.1.3 on 2022-12-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainerprofile',
            options={'permissions': (('sport_app.can_change_article', 'can change article'),)},
        ),
    ]
