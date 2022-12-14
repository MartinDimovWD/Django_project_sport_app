from django.contrib import admin

from project_project.profiles.models import TrainerProfile, TraineeProfile


# Register your models here.
@admin.register(TrainerProfile)
class TrainerProfileAdmin(admin.ModelAdmin):
    list_display = ('profile', 'training_field', 'sports_trained')
    list_filter = ['training_field', 'years_experience', 'phone_number' ]


@admin.register(TraineeProfile)
class TraineeProfileAdmin(admin.ModelAdmin):
    list_display = ['profile',  'height', 'weight', 'experience']
    list_filter = ['height', 'weight', 'experience', ]

