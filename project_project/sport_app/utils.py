from functools import reduce

from project_project.web_app.models import ExerciseRating


def get_avg_rating(entries):
    if entries:
        sum = reduce(lambda a, b: a + b, [int(n.rating) for n in entries])
        avg_rating = sum / len(entries)
        return avg_rating
    else:
        return None


def get_exercise_ratings(exercise):
    entries = ExerciseRating.objects.filter(exercise=exercise)
    return get_avg_rating(entries)

# def get_gym_rating(gym):
#     entries = GymRating.objects.filter(gym=gym)
#     return get_avg_rating(entries)

# def get_trainer_rating(trainer):
#     entries = TrainerRating.objects.filter(gym=trainer)
#     return get_avg_rating(entries)