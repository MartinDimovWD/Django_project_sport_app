import random

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