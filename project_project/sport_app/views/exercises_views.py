from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from project_project.sport_app.forms import CustomExerciseForm
from project_project.sport_app.models import Exercise, CustomExercise


class ExercisesListView(ListView):
    template_name = 'content/exercises/exercises-list.html'
    model = Exercise
    paginate_by = 8
    context_object_name = 'exercises'


class ExerciseDetails(DetailView):
    template_name = 'content/exercises/exercise.html'
    model = Exercise
    context_object_name = 'exercise'



class CustomExerciseCreate(LoginRequiredMixin, CreateView):
    template_name = 'content/exercises/custom/create-exercise.html'
    # model = CustomExercise
    context_object_name = 'custom_exercise'
    form_class = CustomExerciseForm
    success_url = reverse_lazy('my exercises list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CustomExerciseList(LoginRequiredMixin, ListView):
    template_name = 'content/exercises/custom/my-exercises.html'
    model = CustomExercise
    context_object_name = 'custom_exercises'
    paginate_by = 8

    def get_queryset(self):
        custom_exercises = CustomExercise.objects.filter(owner=self.request.user.pk)
        return custom_exercises


class CustomExerciseUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'content/exercises/custom/update-exercise.html'
    model = CustomExercise
    context_object_name = 'custom_exercise'
    form_class = CustomExerciseForm
    success_url = reverse_lazy('my exercises list')


class CustomExerciseDetail(LoginRequiredMixin, DetailView):
    template_name = 'content/exercises/custom/exercise-details.html'
    model = CustomExercise
    context_object_name = 'custom_exercise'


class CustomExerciseDelete(DeleteView):
    template_name = 'content/exercises/custom/exercise-delete.html'
    model = CustomExercise
    context_object_name = 'custom_exercise'

