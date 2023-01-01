from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from project_project.profiles.mixins import TraineeProfileRequiredMixin
from project_project.sport_app.forms import WorkoutForm
from project_project.sport_app.models import Workout


class WorkoutsListView(TraineeProfileRequiredMixin,ListView):
    template_name = 'content/workouts/workout-list.html'
    model = Workout
    paginate_by=9
    context_object_name = 'workouts'

    def get_queryset(self):
        workouts = Workout.objects.order_by('-date')
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
