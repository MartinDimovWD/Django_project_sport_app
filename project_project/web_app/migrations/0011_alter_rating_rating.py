# Generated by Django 4.1.3 on 2023-01-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('1', ''), ('2', ''), ('3', ''), ('4', ''), ('5', '')], default=0, max_length=1, null=True),
        ),
    ]
