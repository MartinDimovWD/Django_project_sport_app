# Generated by Django 4.1.3 on 2023-01-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_app', '0005_alter_goal_date_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='duration',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
