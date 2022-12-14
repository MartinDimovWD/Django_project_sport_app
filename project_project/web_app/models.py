from django.db import models
from django.db.models import Avg

from project_project.accounts.models import AppUser
from project_project.locations.models import Gym
from project_project.profiles.models import TrainerProfile
from project_project.sport_app.models import Article, Exercise


# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def average_rating(self):
        return Rating.objects.filter(self).aggregate(Avg('rating'))['rating__avg']


class ArticleRating(Rating):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class GymRating(Rating):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)


class TrainerRating(Rating):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)


class ExerciseRating(Rating):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
