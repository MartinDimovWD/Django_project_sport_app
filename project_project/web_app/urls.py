from django.urls import path

from project_project.web_app.views import  index_register_view

urlpatterns=[
    path('', index_register_view, name='index register')
]