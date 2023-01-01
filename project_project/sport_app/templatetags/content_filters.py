import random
import time

from django.template import Library

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
    elif exercise.type == 'machine' or exercise.type == 'free weights':
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