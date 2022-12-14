from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinLengthValidator
from django.db import models
from cities_light.models import City

from project_project.web_app.validators import name_only_alpha


class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=20,
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
            ('prefer_not_to_say', 'Prefer not to say')
        ), null=False, blank=False
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.URLField(max_length=400,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            if self.gender == 'male':
                self.profile_picture = 'https://cdn-icons-png.flaticon.com/512/177/177660.png'
            elif self.gender == 'female':
                self.profile_picture = 'https://cdn-icons-png.flaticon.com/512/177/177687.png'
            else:
                self.profile_picture = 'https://i.pinimg.com/originals/c4/b7/3d/c4b73d3e1419c82d0976b48af1a29ab0.png'
        super(AppUser, self).save(*args, **kwargs)


#???????
    # def client_type(self):
        # self.client_type = ''
        # if self.trainerprofile:
        #     self.client_type= 'Coach'
        # elif self.traineeprofile:
        #     self.client_type= 'Trainee'
        # else:
        #     self.client_type = 'Staff'
        # return self.client_type
        # return self.client_type