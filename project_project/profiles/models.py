from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from project_project.accounts.models import AppUser
from project_project.sport_app.models import Goal, Exercise, Sport


class TraineeProfile(models.Model):
    client_type = models.CharField(max_length=30, default='Trainee', null=False, blank=False)
    profile = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    experience = models.CharField(
        max_length=20,
        choices=(
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('amateur', 'Amateur'),
            ('advanced', 'Advanced'),
            ('professional', 'Professional'),
        ), null=False, blank=False
    )
    goals = models.ManyToManyField(Goal, )
    favourite_exercises = models.ManyToManyField(Exercise, )
    favourite_sports = models.ManyToManyField(Sport, )
    def __str__(self):
        return self.profile.full_name

class TrainerProfile(models.Model):
    client_type = models.CharField(max_length=30, null=False,blank=False)
    profile = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    training_field = models.CharField(
        max_length=30,
        choices=(
            ('coach', 'Coach'),
            ('dietitian', 'Dietitian'),
            ('physiologist', 'Physiologist')
        ),
        null=False, blank=False
    )
    # TODO: find out how the years of xp and age can increment each year
    # TODO: validator for years of xp not exceeding the age of the trainer - 18
    years_experience = models.PositiveIntegerField()
    sports = models.ManyToManyField(Sport, )
    bio = models.TextField()
    # TODO: make a validator for phone number with RegEx
    phone_number = models.CharField(max_length=15)

    # TODO: count the number of trainees the trainer has hired them
    # clients = models.ManyToManyField(Trainee, )
    prime_membership = models.BooleanField(default=False)
    # TODO: give trainers permissions to write articles and have them listed in their profile if any.
    def sports_trained(self):
        sports_av = []
        for sport in list(self.sports.all()):
            sports_av.append(sport.sport_name)
        return ", ".join(sports_av)

