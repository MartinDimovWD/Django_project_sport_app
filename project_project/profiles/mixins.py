from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy


class TrainerProfileRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.trainerprofile:
                return super().dispatch(request, *args, **kwargs)
        except:
            return render(request, 'profiles/403-need-coach-prof.html')


class PrimeRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.trainerprofile.prime_membership:
            return render(request, 'profiles/403-need-prime-membership.html')


class TraineeProfileRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            user =request.user.traineeprofile
            return super().dispatch(request, *args, **kwargs)
        except:
            return render(request, 'profiles/403-need-trainee-prof.html')

