from datetime import datetime

from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from project_project.accounts.models import AppUser
from project_project.profiles.mixins import TraineeProfileRequiredMixin
from project_project.sport_app.forms import WorkoutForm
from project_project.sport_app.models import Workout, Exercise, ExerciseInstance


class WorkoutsListView(TraineeProfileRequiredMixin,ListView):
    template_name = 'content/workouts/workout-list.html'
    model = Workout
    paginate_by=9
    context_object_name = 'workouts'

    def get_queryset(self):
        workouts = Workout.objects.filter(owner=self.request.user.pk).order_by('-date')
        return workouts


class WorkoutDetails(TraineeProfileRequiredMixin,DetailView):
    template_name = 'content/workouts/workout-details.html'
    model = Workout
    context_object_name = 'workout'


class WorkoutCreateView(TraineeProfileRequiredMixin,CreateView):
    template_name = 'content/workouts/create-workout.html'
    # model = Workout
    # fields = ['name', 'exercises', 'duration']
    form_class = WorkoutForm
    context_object_name = 'workout'
    success_url = reverse_lazy('workouts list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        name = ''
        day_time = ''
        if datetime.now().strftime('%p') == 'AM':
            day_time = 'morning'
        else:
            day_time = 'afternoon'
        weekday = datetime.now().strftime('%A')
        date = datetime.now().strftime('%d %b %Y')
        name = f'{weekday} {day_time} workout - {date}'
        initials = {
            'name': name
        }
        return initials


class WorkoutUpdateView(TraineeProfileRequiredMixin,UpdateView):
    template_name = 'content/workouts/update-workout.html'
    model = Workout
    form_class = WorkoutForm
    # fields = ['name', 'exercises', 'duration']
    context_object_name = 'workout'
    success_url = reverse_lazy('workouts list')


class WorkoutDeleteView(TraineeProfileRequiredMixin,DeleteView):
    template_name = 'content/workouts/delete-workout.html'
    model = Workout
    fields = []
    context_object_name = 'workout'
    success_url = reverse_lazy('workouts list')


def add_workout(request):
    user = AppUser.objects.get(pk=request.user.pk)
    ExercisesFormset = inlineformset_factory(
        Workout,
        ExerciseInstance,
        fields=('exercise', 'sets','reps', 'weight', 'distance', 'duration'),
        max_num=10,
        extra=3
    )
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = user
            f.save()
            formset = ExercisesFormset(request.POST, instance=f)
            if formset.is_valid():
                formset.save()
                return redirect('workouts list')

    else:
        form = WorkoutForm()
        formset = ExercisesFormset()

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'content/workouts/create-workout.html', context)
