from django.contrib import admin

from project_project.locations.models import Gym, Facility


# Register your models here.
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'gyms_with_this_facility']
    list_display_links = []
    list_editable = []
    search_fields = ['name']


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ['gym_name', 'location', 'get_working_hours','gym_facilities', 'gym_sports_available']
    list_filter=[ 'open_hour', 'close_hour', 'location',]
    list_display_links = []
    list_editable = []
    search_fields = ['gym_name']
    # fieldsets = (
    #     ("Base", {'fields': ('gym_name', 'location',)}),
    # )

