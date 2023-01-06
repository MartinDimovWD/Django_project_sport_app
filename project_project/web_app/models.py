from django.db import models
from django.db.models import Avg

from project_project.accounts.models import AppUser
from project_project.locations.models import Gym
from project_project.profiles.models import TrainerProfile
from project_project.sport_app.models import Article, Exercise


# Create your models here.

class Rating(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    rating = models.CharField(
        max_length=1,
        choices=(
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
        ),
        blank=False,
        null=True,
    )
    comment = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    def average_rating(self):
        return Rating.objects.filter(self).aggregate(Avg('rating'))['rating__avg']


class GymRating(Rating):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)


class TrainerRating(Rating):
    trainer = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)


class ExerciseRating(Rating):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
