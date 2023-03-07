
from django.core.paginator import Paginator
from django.shortcuts import render
from project_project.profiles.models import TrainerProfile

from project_project.sport_app.models import Article, Exercise, CustomExercise, FavouriteExercise, UserReadingList


# TODO: INCLUDE INLINE FORMSETS TO THE WORKOUT SO YOU CAN ADD MULTIPLE EXERCISES

def filter_exercises_by_bodypart(request, bodypart):
    exercises = Exercise.objects.filter(body_parts__contains=bodypart)
    user_faves = []
    if request.user.pk:
        user_faves = [ex.exercise for ex in FavouriteExercise.objects.filter(user=request.user)]
    context = {
        'exercises': exercises,
        'user_faves': user_faves
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
    reading_list =[]
    if request.user.pk:
        reading_list = [art.article for art in UserReadingList.objects.filter(user=request.user)]
    context = {
        'articles': articles,
        'page_obj': page_obj,
        'reading_list': reading_list
    }
    return render(request, 'content/articles/articles-list.html', context)


def filter_trainers_by_location(request, location):
    trainers = TrainerProfile.objects.filter(profile__location__name=location)
    paginator = Paginator(trainers, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'trainers': trainers,
        'page_obj': page_obj
    }
    return render(request, 'profiles/trainer/view-for-trainees/all-trainers.html', context)

# def add_to_favourites(request, pk):
#     exercise = Exercise.objects.get(pk=pk)
#     exercise.owner = request.user
#     return reverse_lazy('exercises list')
