from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.forms import ModelForm, modelformset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from project_project.accounts.models import AppUser
from project_project.locations.models import Gym
from project_project.profiles.models import TrainerProfile
from project_project.sport_app.filters import ArticleCategoryFilter
from project_project.sport_app.forms import WorkoutForm, CustomExerciseForm, ArticleForm, CustomGoalForm
from project_project.sport_app.models import Article, Exercise, Workout, CustomExercise, CustomGoal
from project_project.web_app.utils import QuerySetChain


# Create your views here.
# TODO: INCLUDE INLINE FORMSETS TO THE WORKOUT SO YOU CAN ADD MULTIPLE EXERCISES

class ArticlesListView(ListView):
    template_name = 'content/articles/articles-list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 6
    # queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Article.objects.all()) == 2:
            context['featured'] = Article.objects.all()[0]
            context['featured2'] = Article.objects.all()[1]
        # context['form'] = self.filterset.form
        # TODO: might put featured articles instead of the first 3
        return context

    def get_queryset(self):
        articles = Article.objects.order_by('-publication_date')
        return articles


class ArticleDetails(DetailView):
    template_name = 'content/articles/article.html'
    model = Article
    context_object_name = 'article'


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = 'content/articles/create-article.html'
    form_class = ArticleForm
    # model = Article
    # fields = ['heading', 'abstract', 'body', 'article_image', 'category']
    context_object_name = 'article'
    success_url = reverse_lazy('articles list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExercisesListView(ListView):
    template_name = 'content/exercises/exercises-list.html'
    model = Exercise
    paginate_by = 8
    context_object_name = 'exercises'


class ExerciseDetails(DetailView):
    template_name = 'content/exercises/exercise.html'
    model = Exercise
    context_object_name = 'exercise'


class CustomGoalCreate(LoginRequiredMixin, CreateView):
    template_name = 'content/custom_goal/create.html'
    # model = CustomExercise
    context_object_name = 'custom_goal'
    form_class = CustomGoalForm
    success_url = reverse_lazy('index register')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.base_goal = False
        return super().form_valid(form)


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


class CustomExerciseDetail(LoginRequiredMixin, DetailView):
    template_name = 'content/exercises/custom/exercise-details.html'
    model = CustomExercise
    context_object_name = 'custom_exercise'


class CustomExerciseDelete(DeleteView):
    template_name = 'content/exercises/custom/exercise-delete.html'
    model = CustomExercise
    context_object_name = 'custom_exercise'


class TrainersListView(ListView):
    template_name = 'profiles/trainer/view-for-trainees/all-trainers.html'
    model = TrainerProfile
    paginate_by = 6
    context_object_name = 'trainers'


class TrainerDetails(DetailView):
    template_name = 'profiles/trainer/view-for-trainees/trainer-details.html'
    model = TrainerProfile
    context_object_name = 'trainer'


class WorkoutsListView(ListView):
    template_name = 'content/workouts/workout-list.html'
    model = Workout
    paginate_by=9
    context_object_name = 'workouts'

    def get_queryset(self):
        workouts = Workout.objects.order_by('-date')
        return workouts


class WorkoutDetails(DetailView):
    template_name = 'content/workouts/workout-details.html'
    model = Workout
    context_object_name = 'workout'


class WorkoutCreateView(CreateView):
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


class WorkoutUpdateView(UpdateView):
    template_name = 'content/workouts/update-workout.html'
    model = Workout
    form_class = WorkoutForm
    # fields = ['name', 'exercises', 'duration']
    context_object_name = 'workout'
    success_url = reverse_lazy('workouts list')


class WorkoutDeleteView(DeleteView):
    template_name = 'content/workouts/delete-workout.html'
    model = Workout
    fields = []
    context_object_name = 'workout'
    success_url = reverse_lazy('workouts list')


def filter_exercises_by_bodypart(request, bodypart):
    exercises = Exercise.objects.filter(body_parts__contains=bodypart)
    context = {
        'exercises': exercises
    }
    return render(request, 'content/exercises/exercises-list.html', context)


def filter_custom_exercises_by_bodypart(request, bodypart):
    exercises = CustomExercise.objects.filter(body_parts__contains=bodypart)
    context = {
        'exercises': exercises
    }
    return render(request, 'content/exercises/custom/my-exercises.html', context)

def filter_articles_by_category(request, category):
    articles = Article.objects.filter(category__contains=category)
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'page_obj': page_obj
    }
    return render(request, 'content/articles/articles-list.html', context)


# def add_to_favourites(request, pk):
#     exercise = Exercise.objects.get(pk=pk)
#     exercise.owner = request.user
#     return reverse_lazy('exercises list')
