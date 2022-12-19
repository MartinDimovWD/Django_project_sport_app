from django.shortcuts import render, redirect

from project_project.accounts.models import AppUser
from project_project.profiles.models import TrainerProfile, TraineeProfile


def index_register_view(request):
    if request.user.pk:
        return redirect('articles list')
    return render(request, 'account/index-sign-up.html')
