from django import forms
from django.contrib.auth import logout
from django.forms import ModelForm, HiddenInput
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from project_project.accounts.models import AppUser
from project_project.profiles.forms import TraineeProfileForm, TrainerProfileForm
from project_project.profiles.models import TrainerProfile, TraineeProfile
from project_project.sport_app.models import Goal, CustomGoal, Workout


class CompleteTrainerProfileForm(ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ('client_type', 'profile', 'training_field','years_experience','sports','bio','phone_number')
        widgets = {'profile': HiddenInput(),
                   'client_type': HiddenInput(),
                   'training_field': forms.Select(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'years_experience': forms.NumberInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'sports': forms.SelectMultiple(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'phone_number': forms.NumberInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': 'xxx-xxx-xxx',
                        }),
                    'bio': forms.Textarea(
                        attrs={
                            'class': 'form-control',
                            'placeholder': 'Include any relevant professional experience. You can include certifications, testimonials, etc.',
                        })

                }


def complete_trainer_profile_view(request):
    client_pk = request.user.pk
    # the request.user is passed in the profile field with the initial attr, so the profile is attached to the account.
    # the profile is removed from the form as it give the option to pick among all other users.
    form = CompleteTrainerProfileForm(initial={'client_type': 'Trainer', 'profile': AppUser.objects.get(pk=client_pk)})
    # form = CompleteTrainerProfileForm({'profile': AppUser.objects.get(pk=client_pk)})
    if request.method == 'POST':
        form = CompleteTrainerProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index register')
    context = {'form': form}
    return render(request, 'profiles/trainer/complete-profile.html', context)


class CompleteTraineeProfileForm(ModelForm):
    class Meta:
        model = TraineeProfile
        fields = ('client_type', 'profile', 'height','weight','experience','goals')
        widgets = {'profile': HiddenInput(),
                   'client_type': HiddenInput(),
                   'height': forms.NumberInput(
                       attrs={
                           'class': 'form-control',
                           'placeholder': '---',
                       }),
                   'weight': forms.NumberInput(
                       attrs={
                           'class': 'form-control',
                           'placeholder': '---',
                       }),
                   'experience': forms.Select(
                       attrs={
                           'class': 'form-control',
                           'placeholder': '---',
                       }),
                   'goals': forms.SelectMultiple(
                       attrs={
                           'class': 'form-control',
                           'placeholder': '---',
                       })
                   }

    def __init__(self,*args,**kwargs):
        super(CompleteTraineeProfileForm,self).__init__(*args,**kwargs)
        self.fields['goals'].queryset = Goal.objects.filter(base_goal=True)

def complete_trainee_profile_view(request):
    client_pk = request.user.pk
    form = CompleteTraineeProfileForm(initial={'client_type': 'Trainee', 'profile': AppUser.objects.get(pk=client_pk)})
    if request.method == 'POST':
        form = CompleteTraineeProfileForm(request.POST)
        if form.is_valid():
            for goal in list(form.cleaned_data['goals']):
                CustomGoal.objects.create(owner=AppUser.objects.get(pk=client_pk), goal_name=goal.goal_name, base_goal=False)
            form.save()
            return redirect('index register')
    context = {'form': form}
    return render(request, 'profiles/trainee/complete-profile.html', context)


class UpdateTrainerProfileView(UpdateView):
    model = TrainerProfile
    form_class = TrainerProfileForm
    # fields = ['training_field', 'years_experience', 'bio', 'phone_number']
    template_name = 'profiles/trainer/update-profile.html'
    success_url = '/'

    def get_success_url(self):
        return reverse_lazy('trainer profile details', kwargs={'pk': self.object.pk})


class TrainerProfileView(DetailView):
    template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
    model = TrainerProfile
    context_object_name = 'trainer'


class TrainerPersonalProfileView(DetailView):
    template_name = 'profiles/trainer/view-for-trainers/trainer-details.html'
    model = TrainerProfile
    # context_object_name = 'trainer'


class UpdateTraineeProfileView(UpdateView):
    model = TraineeProfile
    form_class = TraineeProfileForm
    # fields = ['height', 'weight', 'experience', 'goals']
    template_name = 'profiles/trainee/update-profile.html'

    def get_success_url(self):
        return reverse_lazy('trainee profile details', kwargs={'pk': self.object.pk})


class TraineeProfileView(DetailView):
    template_name = 'profiles/trainee/profile-details.html'
    model = TraineeProfile

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goal.objects.filter(base_goal=False, owner=self.request.user.pk)
        user_workouts = Workout.objects.filter(owner=self.request.user.pk).order_by('-pk')
        context['last_workouts'] = user_workouts
        if len(user_workouts)>=1:
            context['last_workout_one'] = user_workouts[0]
        if len(user_workouts)>=2:
            context['last_workout_two'] = user_workouts[1]
        if len(user_workouts)>=3:
            context['last_workout_three'] = user_workouts[2]
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


