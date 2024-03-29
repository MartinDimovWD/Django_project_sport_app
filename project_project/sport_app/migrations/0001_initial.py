# Generated by Django 4.1.3 on 2023-05-01 17:34

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
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('article_image', models.URLField(blank=True, null=True)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Exercises', 'Exercises'), ('Nutrition', 'Nutrition'), ('Supplements', 'Supplements'), ('Programmes', 'Programmes'), ('Interviews', 'Interviews'), ('Training', 'Training'), ('Science', 'Science'), ('Equipment', 'Equipment and Clothing')], max_length=1000)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('bodyweight', 'bodyweight'), ('machine', 'machine'), ('free_weights', 'free weights'), ('cardio', 'cardio')], max_length=30)),
                ('body_parts', multiselectfield.db.fields.MultiSelectField(choices=[('Legs', 'Legs'), ('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Back', 'Back'), ('Chest', 'Chest'), ('Core', 'Core'), ('full_body', 'Full Body')], max_length=50)),
                ('exercise_photo', models.URLField(blank=True, null=True)),
                ('metric', models.CharField(choices=[('distance', 'distance'), ('weight', 'weight'), ('time', 'time')], max_length=30)),
                ('quantity', models.CharField(choices=[('kilometers', 'kilometers'), ('reps', 'reps'), ('duration', 'duration')], max_length=30)),
                ('base_exercise', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=200)),
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
                ('date_finished', models.DateTimeField(blank=True, null=True)),
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
                ('duration', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserReadingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='sport_app.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='sport_app.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('reps', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('distance', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('duration', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_app.exercise')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport_app.workout')),
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
