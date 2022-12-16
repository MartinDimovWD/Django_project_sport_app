from django.contrib import admin

from project_project.profiles.models import TrainerProfile, TraineeProfile


# Register your models here.
@admin.register(TrainerProfile)
class TrainerProfileAdmin(admin.ModelAdmin):
    list_display = ['profile', 'training_field', 'sports_trained', 'prime_membership']
    list_filter = ['training_field',  'prime_membership']
    list_display_links = []
    list_editable = []
    search_fields = ['training_field']
    # fieldsets = (
    #     ("Base", {'fields': ('gym_name', 'location',)}),
    # )
@admin.register(TraineeProfile)
class TraineeProfileAdmin(admin.ModelAdmin):
    list_display = ['profile',  'height', 'weight', 'experience']
    list_filter = ['experience', ]
    list_display_links = []
    list_editable = []
    search_fields = ['experience']
    # fieldsets = (
    #     ("Base", {'fields': ('gym_name', 'location',)}),
    # )
