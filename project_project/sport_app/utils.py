from functools import reduce

from project_project.web_app.models import ExerciseRating, GymRating, TrainerRating


def get_avg_rating(entries):
    if entries:
        sum = reduce(lambda a, b: a + b, [int(n.rating) for n in entries])
        avg_rating = sum / len(entries)
        return avg_rating
    else:
        return None


def get_exercise_avg_ratings(exercise):
    entries = ExerciseRating.objects.filter(exercise=exercise)
    if entries:
        return get_avg_rating(entries)
    else:
        return 0


def get_gym_avg_ratings(gym):
    entries = GymRating.objects.filter(gym=gym)
    return get_avg_rating(entries)


def get_trainer_avg_ratings(trainer):
    entries = TrainerRating.objects.filter(trainer=trainer)
    return get_avg_rating(entries)


