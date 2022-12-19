from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from project_project.accounts.forms import AppUserUpdateForm, ClientSignUpForm
from project_project.accounts.models import AppUser
from project_project.web_app.field_validators import age_validator


def combined_sign_up_view(request):
    return render(request, 'account/register-page.html')


class TrainerSignUpView(CreateView):
    template_name = 'account/trainer/sign-up.html'
    form_class = ClientSignUpForm
    success_url = reverse_lazy('trainer complete profile')

    def form_valid(self, form):
        user = form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('trainer complete profile')


class TraineeSignUpView(CreateView):
    template_name = 'account/trainee/sign-up.html'
    form_class = ClientSignUpForm
    success_url = reverse_lazy('trainee complete profile')

    def form_valid(self, form):
        user = form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('trainee complete profile')


class SignInView(LoginView):
    template_name = 'account/login.html'
    next_page = reverse_lazy('index register')


class SignOutView(LoginRequiredMixin, LogoutView):
    template_name = 'account/sign-out.html'
    next_page = reverse_lazy('index register')


class UpdatePersonalView(UpdateView):
    model = AppUser
    form_class = AppUserUpdateForm
    # fields = ['height', 'weight', 'experience', 'goals']
    template_name = 'profiles/account/update-personal.html'

    def get_success_url(self):
        try:
            pk = self.object.traineeprofile.pk
            return reverse_lazy('trainee profile details', kwargs={'pk': pk})
        except:
            pk = self.object.trainerprofile.pk
            return reverse_lazy('trainer profile details', kwargs={'pk': pk})

