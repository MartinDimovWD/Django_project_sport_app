import random
import time

from django.template import Library

from project_project.locations.models import Gym
from project_project.profiles.utils import get_times_hired_coach, check_for_active_contract
from project_project.sport_app.models import ExerciseInstance
from project_project.sport_app.utils import get_gym_avg_ratings, get_exercise_avg_ratings, get_trainer_avg_ratings
from project_project.web_app.models import GymRating

register = Library()


@register.filter('capitalize_each_word')
def capitalize_each_word(str):
    return " ".join([x.capitalize() for x in str.split()])


@register.filter('random_reps')
def random_reps(exercise):
    reps = random.randint(7, 14)
    sets = random.randint(3, 5)
    weight = random.randint(5,40)
    duration = random.randint(10, 40)
    if exercise.type == 'bodyweight':
        return f'{sets} sets X {reps} reps'
    elif exercise.type == 'machine' or exercise.type == 'free_weights':
        return f'{sets} sets X {reps} reps X {weight} kg'
    elif exercise.type == 'cardio':
        return f'Duration: {duration} minutes'


@register.filter('open_now')
def open_now(gym):
    current_hour = int(time.strftime('%H'))
    if gym.open_hour <= current_hour <= gym.close_hour:
        return True


@register.filter('date_convert')
def date_convert(date):
    return date.strftime('%d %b %Y - %I %p')


@register.filter('get_exercises_of_workout')
def get_exercises_of_workout(workout):
    exercises = ExerciseInstance.objects.filter(workout=workout)
    return exercises


@register.filter('listview_times_hired')
def listview_times_hired(coach):
    return get_times_hired_coach(coach.profile)

@register.filter('times')
def times(number):
    return range(number)

@register.filter('join_vertical_bar')
def join_vertical_bar(q):
    return ' | '.join(q)

@register.filter('get_gym_rating')
def get_gym_rating(gym):
    if get_gym_avg_ratings(gym):
        return int(get_gym_avg_ratings(gym))
    return 0

@register.filter('get_exercise_rating')
def get_exercise_rating(exercise):
    if get_exercise_avg_ratings(exercise):
        return int(get_exercise_avg_ratings(exercise))
    return 0

@register.filter('get_trainer_rating')
def get_trainer_rating(trainer):
    if get_trainer_avg_ratings(trainer):
        return int(get_trainer_avg_ratings(trainer))
    return 0