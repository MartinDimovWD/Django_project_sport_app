from functools import reduce

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.edit import FormMixin, ModelFormMixin

from project_project.sport_app.forms import CustomExerciseForm
from project_project.sport_app.models import Exercise, CustomExercise, FavouriteExercise, Article, UserReadingList
from project_project.sport_app.utils import get_exercise_avg_ratings
from project_project.web_app.forms import RatingForm, ExerciseRatingForm
from project_project.web_app.models import ExerciseRating


class ExercisesListView(ListView):
    template_name = 'content/exercises/exercises-list.html'
    model = Exercise
    paginate_by = 8
    context_object_name = 'exercises'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.pk:
            user_faves = [ex.exercise for ex in FavouriteExercise.objects.filter(user=self.request.user)]
            context['user_faves'] = user_faves
        return context

    def get_queryset(self):
        queryset = Exercise.objects.filter(base_exercise=True)
        return queryset

# class ExerciseDetails(ModelFormMixin, DetailView):
#     template_name = 'content/exercises/exercise.html'
#     model = Exercise
#     context_object_name = 'exercise'
#     form_class = RatingForm
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ExerciseDetails, self).get_context_data(**kwargs)
#         user_faves = [ex.exercise for ex in FavouriteExercise.objects.filter(user=self.request.user)]
#         context['user_faves'] = user_faves
#         return context

def exercise_details(request, slug):
    exercise = Exercise.objects.get(slug=slug)
    rating = get_exercise_avg_ratings(exercise)
    rtgs = ExerciseRating.objects.filter(exercise=exercise)
    context = {
        'exercise': exercise,
        'rating': rating,
        'rtgs': rtgs,
        'yellow_stars': int(rating),
        'grey_stars': 5 - int(rating),
    }

    if request.user.pk:
        has_user_rating = ExerciseRating.objects.filter(exercise=exercise, user=request.user)
        context['has_user_rating'] = has_user_rating
        # user_faves = [ex.exercise for ex in FavouriteExercise.objects.filter(user=request.user)]
        # context['user_faves'] = user_faves
        if not has_user_rating:
            if request.method == 'POST':
                form = ExerciseRatingForm(request.POST)
                if form.is_valid():
                    f = form.save(commit=False)
                    f.user = request.user
                    f.exercise = exercise
                    f.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                form = RatingForm()
            context['form'] = form

    return render(request, 'content/exercises/exercise.html', context)


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


@login_required
def add_to_favourites_exercise(request, pk):
    exercise = Exercise.objects.get(pk=pk)
    user_favourite_exercises = FavouriteExercise.objects.filter(exercise=exercise, user=request.user)
    if user_favourite_exercises:
        user_favourite_exercises.delete()
    else:
        FavouriteExercise.objects.create(exercise=exercise, user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


