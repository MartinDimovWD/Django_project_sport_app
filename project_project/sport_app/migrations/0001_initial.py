# Generated by Django 4.1.3 on 2022-12-14 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('bodyweight', 'bodyweight'), ('machine', 'machine'), ('free_weights', 'free weights'), ('cardio', 'cardio')], max_length=30)),
                ('body_parts', multiselectfield.db.fields.MultiSelectField(choices=[('Legs', 'Legs'), ('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Back', 'Back'), ('Chest', 'Chest'), ('Core', 'Core'), ('full_body', 'Full Body')], max_length=30)),
                ('exercise_photo', models.URLField(blank=True, null=True)),
                ('metric', models.CharField(choices=[('distance', 'distance'), ('weight', 'weight'), ('time', 'time')], max_length=30)),
                ('quantity', models.CharField(choices=[('kilometers', 'kilometers'), ('reps', 'reps'), ('duration', 'duration')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=30)),
                ('is_accomplished', models.BooleanField(default=False)),
                ('base_goal', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_name', models.CharField(max_length=20)),
                ('is_group_sport', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
                ('sport_photo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomGoal',
            fields=[
                ('goal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sport_app.goal')),
            ],
            bases=('sport_app.goal',),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('exercises', models.ManyToManyField(to='sport_app.exercise')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('article_image', models.URLField()),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Exercises', 'Exercises'), ('Nutrition', 'Nutrition'), ('Supplements', 'Supplements'), ('Programmes', 'Programmes'), ('Interviews', 'Interviews'), ('Training', 'Training'), ('Science', 'Science'), ('Equipment', 'Equipment and Clothing')], max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomExercise',
            fields=[
                ('exercise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sport_app.exercise')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('sport_app.exercise',),
        ),
    ]
