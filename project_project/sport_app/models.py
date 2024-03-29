from datetime import datetime

from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from multiselectfield import MultiSelectField

from project_project.accounts.models import AppUser


class Sport(models.Model):
    sport_name = models.CharField(
        max_length=20,
        null=False, blank=False
    )

    is_group_sport = models.BooleanField(
        null=False, blank=False)
    description = models.TextField(
        null=True,
        blank=True
    )

    sport_photo = models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.sport_name


class Goal(models.Model):
    goal_name = models.CharField(
        max_length=30,
        null=False, blank=False
    )
    is_accomplished = models.BooleanField(default=False)
    base_goal = models.BooleanField(default=True)
    description = models.TextField(
        null=True,
        blank=True
    )
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(
        null=True,
        blank=True
    )
    def __str__(self):
        return self.goal_name

    def save(self, *args, **kwargs):
        if self.is_accomplished==True:
            self.date_finished = datetime.now()
            print('noise')
        super(Goal, self).save(*args, **kwargs)

# custom goals are those that users has created, and they are only accessible to them
class CustomGoal(Goal):
    pass


class Exercise(models.Model):
    name = models.CharField(
        max_length=30,
        null=False, blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=30,
        choices=(
            ('bodyweight', 'bodyweight'),
            ('machine', 'machine'),
            ('free_weights', 'free weights'),
            ('cardio', 'cardio')
        ),
        null=False, blank=False
    )
    body_parts = MultiSelectField(
        max_length=50,
        choices=(
            ('Legs', 'Legs'),
            ('Shoulders', 'Shoulders'),
            ('Arms', 'Arms'),
            ('Back', 'Back'),
            ('Chest', 'Chest'),
            ('Core', 'Core'),
            ('full_body', 'Full Body')
        ),
        null=False, blank=False
    )
    exercise_photo = models.URLField(
        null=True,
        blank=True
    )
    # rating = models.PositiveIntegerField(default=None)
    # TODO: if default is None show empty stars. Make a function that once receiving a rating, calculates the average and shows it
    metric = models.CharField(
        max_length=30,
        choices=(
            ('distance', 'distance'),
            ('weight', 'weight'),
            ('time', 'time')
        ),
        null=False, blank=False
    )
    quantity = models.CharField(
        max_length=30,
        choices=(
            ('kilometers', 'kilometers'),
            ('reps', 'reps'),
            ('duration', 'duration')
        ),
        null=False, blank=False
    )
    base_exercise = models.BooleanField(default=True)
    slug = models.SlugField(
        max_length=200,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name



# Custom exercises are those created by the user, and they are only accessible to them
class CustomExercise(Exercise):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE )

    def save(self, *args, **kwargs):
        self.base_exercise = False
        if not self.exercise_photo:
            self.exercise_photo = 'https://i.pinimg.com/originals/c4/b7/3d/c4b73d3e1419c82d0976b48af1a29ab0.png'
        super(CustomExercise, self).save(*args,**kwargs)

class Article(models.Model):
    # TODO: find out how you can hardcode this
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    heading = models.CharField(
        max_length=100,
        null=False, blank=False
    )
    abstract = models.CharField(
        max_length=300,
    )
    body = models.TextField(
        null=False,
        blank=False
    )
    publication_date = models.DateTimeField(auto_now_add=True)
    article_image = models.URLField(null=True,blank=True)
    category = MultiSelectField(
        max_length=1000,
        choices=(
            ('Exercises', 'Exercises'),
            ('Nutrition', 'Nutrition'),
            ('Supplements', 'Supplements'),
            ('Programmes', 'Programmes'),
            ('Interviews', 'Interviews'),
            ('Training', 'Training'),
            ('Science', 'Science'),
            ('Equipment', 'Equipment and Clothing'),
        ),
        null=False, blank=False
    )
    # rating = models.PositiveIntegerField(default=None)
    # TODO: if default is None show empty stars. Make a function that once receiving a rating, calculates the average and shows it
    slug = models.SlugField(
        max_length=200,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.heading}')
        if not self.article_image:
            self.article_image = 'https://newportfilm.com/wp-content/uploads/2013/07/insta20NDN20venus26serena20april202013.jpg'
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.heading


class Workout(models.Model):
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=60,
        null=False, blank=False,
    )
    date = models.DateTimeField(auto_now_add=True)

    duration = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True
    )
    # exercises = models.ManyToManyField(Exercise, )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            day_time = ''
            if datetime.now().strftime('%p') == 'AM':
                day_time = 'morning'
            else:
                day_time = 'afternoon'
            weekday = datetime.now().strftime('%A')
            date = datetime.now().strftime('%d %b %Y')
            self.name = f'{weekday} {day_time} workout - {date}'
        super(Workout, self).save(*args, **kwargs)


class ExerciseInstance(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    reps = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    weight = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    distance = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    duration = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.exercise.name


class FavouriteExercise(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )

    user = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT
    )


class UserReadingList(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )

    user = models.ForeignKey(
        AppUser,
        on_delete=models.RESTRICT
    )