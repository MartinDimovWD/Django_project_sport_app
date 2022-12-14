from django.contrib import admin

from project_project.accounts.models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'location', 'date_joined']


