from cities_light.models import City
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify

from project_project.sport_app.models import Sport


class Facility(models.Model):
    name = models.CharField(
        max_length=30,
        null=False, blank=False, unique=True
    )

    class Meta:
        verbose_name_plural = 'facilities'

    def __str__(self):
        return self.name

    def gyms_with_this_facility(self):
        gyms_num = len(Gym.objects.filter(facilities=self.pk))
        return gyms_num


class Gym(models.Model):
    gym_name = models.CharField(
        max_length=40,
        null=False, blank=False
    )
    logo = models.URLField(
        null=True,
        blank=True
    )
    location = models.ForeignKey(City, on_delete=models.CASCADE)

    sports_available = models.ManyToManyField(Sport,)
    open_hour = models.PositiveIntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(23)
        ),
        null=False,
        blank=False
    )
    close_hour = models.PositiveIntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(24)
        ),
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True)
    facilities = models.ManyToManyField(Facility,)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=False,
        blank=True,
    )
    # rating = models.PositiveIntegerField(default=None)
    # TODO: if default is None show empty stars. Make a function that once receiving a rating, calculates the average and shows it
    def __str__(self):
        return self.gym_name

    def get_working_hours(self):
        # TODO: raise exception if the closing time is less that the  opening time
        working_hours = f'{self.open_hour} - {self.close_hour}'
        return working_hours

    def gym_facilities(self):
        gym_fac = []
        for fac in list(self.facilities.all()):
            gym_fac.append(fac.name)
        return ", ".join(gym_fac)

    def gym_sports_available(self):
        sports_av = []
        for sport in list(self.sports_available.all()):
            sports_av.append(sport.sport_name)
        return ", ".join(sports_av)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.gym_name}-{self.location}')
        return super().save(*args, **kwargs)