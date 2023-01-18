import re

from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, HiddenInput, formset_factory, modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.edit import FormMixin

from project_project.accounts.models import AppUser
from project_project.profiles.forms import TraineeProfileUpdateForm, TrainerProfileUpdateForm, CompleteTrainerProfileForm, \
    CompleteTraineeProfileForm, ManagePrimeSubscriptionForm
from project_project.profiles.mixins import TrainerProfileRequiredMixin
from project_project.profiles.models import TrainerProfile, TraineeProfile, Contract
from project_project.profiles.utils import check_for_active_contract, get_times_hired_coach, get_num_active_contracts_coach, \
    get_active_trainees, get_goals_active_trainees
from project_project.sport_app.forms import CustomGoalForm, CompleteGoalForm
from project_project.sport_app.models import Goal, CustomGoal, Workout, UserReadingList, FavouriteExercise, Article


def complete_trainer_profile_view(request):
    client_pk = request.user.pk
    # the request.user is passed in the profile field with the initial attr, so the profile is attached to the account.
    # the profile is removed from the form as it give the option to pick among all other users.
    form = CompleteTrainerProfileForm(initial={'client_type': 'Trainer', 'profile': AppUser.objects.get(pk=client_pk)})
    # form = CompleteTrainerProfileForm({'profile': AppUser.objects.get(pk=client_pk)})
    if request.method == 'POST':
        form = CompleteTrainerProfileForm(request.POST)
        if form.is_valid():
            trainer = form.save()
            return redirect('trainer profile details', slug=trainer.slug)
    context = {'form': form}
    return render(request, 'profiles/trainer/complete-profile.html', context)


def complete_trainee_profile_view(request):
    client_pk = request.user.pk
    form = CompleteTraineeProfileForm(initial={'client_type': 'Trainee', 'profile': AppUser.objects.get(pk=client_pk)})
    if request.method == 'POST':
        form = CompleteTraineeProfileForm(request.POST)
        if form.is_valid():
            for goal in list(form.cleaned_data['goals']):
                CustomGoal.objects.create(owner=AppUser.objects.get(pk=client_pk), goal_name=goal.goal_name, base_goal=False)
            trainee = form.save()
            return redirect('trainee profile details', slug=trainee.slug)
    context = {'form': form}
    return render(request, 'profiles/trainee/complete-profile.html', context)


class UpdateTrainerProfileView(UpdateView):
    model = TrainerProfile
    form_class = TrainerProfileUpdateForm
    # fields = ['training_field', 'years_experience', 'bio', 'phone_number']
    template_name = 'profiles/trainer/update-profile.html'
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('trainer profile details', kwargs={'slug': self.object.slug})



class TrainerProfileView(DetailView):
    template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
    model = TrainerProfile
    context_object_name = 'trainer'

    def get_success_url(self):
        return reverse_lazy('trainer details', kwargs={'slug': self.object.slug})


class TrainerPersonalProfileView(DetailView):
    template_name = 'profiles/trainer/view-for-trainers/trainer-details.html'
    model = TrainerProfile
    # context_object_name = 'trainer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        coach = self.request.user
        times_hired = get_times_hired_coach(coach)
        context['times_hired'] = times_hired
        num_active_clients = get_num_active_contracts_coach(coach)
        context['num_active_clients'] = num_active_clients
        active_trainees = get_active_trainees(coach)
        context['active_trainees'] = active_trainees
        trainee_goals = get_goals_active_trainees(coach)
        context['trainee_goals'] = trainee_goals
        trainer_articles = Article.objects.filter(author=coach)
        context['trainer_articles'] = trainer_articles
        is_partner = coach.trainerprofile.prime_membership
        context['is_partner'] = is_partner
        return context


class UpdateTraineeProfileView(LoginRequiredMixin, UpdateView):
    model = TraineeProfile
    form_class = TraineeProfileUpdateForm
    # fields = ['height', 'weight', 'experience', 'goals']
    template_name = 'profiles/trainee/update-profile.html'

    def get_success_url(self):
        return reverse_lazy('trainee profile details', kwargs={'slug': self.object.slug})

    def get_object(self,*args,**kwargs):
        return self.request.user

class TraineeProfileView(FormMixin, DetailView):
    template_name = 'profiles/trainee/profile-details.html'
    model = TraineeProfile
    form_class = CompleteGoalForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['goals'] = Goal.objects.filter(base_goal=False, owner=self.request.user.pk)
        user_workouts = Workout.objects.filter(owner=self.request.user.pk).order_by('-pk')
        context['last_workouts'] = user_workouts
        reading_list = [art.article for art in UserReadingList.objects.filter(user=self.request.user)]
        context['reading_list'] = reading_list
        user_faves = [ex.exercise for ex in FavouriteExercise.objects.filter(user=self.request.user)]
        context['user_faves'] = user_faves
        if len(user_workouts)>=1:
            context['last_workout_one'] = user_workouts[0]
        if len(user_workouts)>=2:
            context['last_workout_two'] = user_workouts[1]
        if len(user_workouts)>=3:
            context['last_workout_three'] = user_workouts[2]
        return context


class TraineeDetailsViewForTrainers(DetailView):
    template_name = 'profiles/trainee/trainee-details.html'
    model = TraineeProfile
    context_object_name = 'trainee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trainee = self.object.profile.pk
        context['goals'] = Goal.objects.filter(owner=trainee)
        context['workouts'] = Workout.objects.filter(owner=trainee)
        return context

class TraineeDeleteView(DeleteView):
    template_name = 'profiles/trainee/profile-delete.html'
    model = TraineeProfile
    fields = []
    context_object_name = 'profile'
    success_url = reverse_lazy('index register')

    def form_valid(self, form):
        logout(self.request)
        return redirect('index register')


class TrainerDeleteView(DeleteView):
    template_name = 'profiles/trainer/profile-delete.html'
    model = TrainerProfile
    fields = []
    context_object_name = 'profile'
    success_url = reverse_lazy('index register')

    def form_valid(self, form):
        logout(self.request)
        return redirect('index register')


class ManagePrimeSubscriptionView(UpdateView):
    template_name = 'profiles/trainer/view-for-trainers/manage-prime.html'
    form_class = ManagePrimeSubscriptionForm
    model = TrainerProfile

    def get_success_url(self):
        return reverse_lazy('trainer profile details', kwargs={'slug': self.object.slug})


@login_required
def hire_coach_view(request, coach_pk):
    trainee = request.user
    coach = AppUser.objects.get(pk=coach_pk)
    active_contract = check_for_active_contract(trainee, coach)
    if not active_contract:
        Contract.objects.create(client=trainee, coach=coach, is_active=True)
    else:
        Contract.objects.get(client=trainee, coach=coach, is_active=True).terminate()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # if there is no active contract, a new one is created


