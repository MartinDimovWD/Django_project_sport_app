# Generated by Django 4.1.3 on 2023-05-01 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
        ('sport_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', ''), ('2', ''), ('3', ''), ('4', ''), ('5', '')], max_length=1, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web_app.rating')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.trainerprofile')),
            ],
            bases=('web_app.rating',),
        ),
        migrations.CreateModel(
            name='GymRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web_app.rating')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.gym')),
            ],
            bases=('web_app.rating',),
        ),
        migrations.CreateModel(
            name='ExerciseRating',
            fields=[
                ('rating_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web_app.rating')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_app.exercise')),
            ],
            bases=('web_app.rating',),
        ),
    ]
