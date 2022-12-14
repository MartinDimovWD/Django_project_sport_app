from django.shortcuts import render

from project_project.accounts.models import AppUser
from project_project.profiles.models import TrainerProfile, TraineeProfile


def index_register_view(request):

    return render(request, 'account/index-sign-up.html')
