from django.contrib import admin

from project_project.accounts.models import AppUser


# Register your models here.
@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name', 'location', 'date_joined', 'is_active']
    list_filter = []
    list_display_links = []
    list_editable = []
    search_fields = ['email', 'first_name', 'last_name', 'username']
    fieldsets = (
        ("Personal Info",
         {'fields': (
             'first_name', 'last_name', 'email', 'username', 'gender', 'location', 'profile_picture'
         )}),
        ("Account Info",
        {'fields': (
            'is_active', 'last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
        )}),
    )

