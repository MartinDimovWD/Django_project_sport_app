from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project_project.web_app.urls')),
    path('auth/', include('project_project.accounts.urls')),
    path('profiles/', include('project_project.profiles.urls')),
    path('locations/', include('project_project.locations.urls')),
    path('sport-app/', include('project_project.sport_app.urls')),

]
