from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(
        max_length=200,
        null=False,
        blank=True,
    )
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.profile.username}')
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.profile.full_name

    def get_favourite_exercises(self):
        pass

    def get_goals(self):
        return Goal.objects.filter(owner=self.profile.pk)


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
    slug = models.SlugField(
        max_length=200,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.profile.username}')
        return super().save(*args, **kwargs)
    def sports_trained(self):
        sports_av = []
        for sport in list(self.sports.all()):
            sports_av.append(sport.sport_name)
        return ", ".join(sports_av)

    def __str__(self):
        return self.profile.full_name


class Contract(models.Model):
    client = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='+')
    coach = models.ForeignKey(AppUser, on_delete=models.RESTRICT, related_name='+')
    sign_date = models.DateTimeField(auto_now_add=True)
    # end_date = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def terminate(self):
        self.is_active=False
        self.save()

    def __str__(self):
        status = ''
        if self.is_active:
            status = 'Active'
        else:
            status = 'Inactive'
        return f'{status} contract between {self.client} and {self.coach}'
    # users can send each other direct messages only if they have a contract.
    # Otherwise, they can only book a meeting

    # TODO: the trainee will send a hire request that will show up
    # as a notification that the coach needs to accept for the contract to
    # be signed
