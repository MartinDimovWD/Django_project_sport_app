from django.core.exceptions import ValidationError


def name_only_alpha(str):
    if not str.isalpha():
        raise ValidationError(
            'Your name can only have alphabetic characters'
        )

def phone_number_10_digits_starts_with_0(num):
    if not num.isnumeric():
        raise ValidationError('Please enter only numbers')
    if not int(num[0]) == 0:
        raise ValidationError('Phone numbers should start with `0`')
    if not len(str(num))==10:
        raise ValidationError('Phone numbers should have 10 digits')


def validate_years_experience(num):
    pass

def age_less_than_100(num):
    if num > 120:
        raise ValidationError('You should take it easier!')


def height_mt_100_lt_240(num):
    if num > 240 and num < 100:
        raise ValidationError('Please measure your height in centimeters')


def weight_mt_40_lt_200(num):
    if num > 200 and num < 40:
        raise ValidationError('Please measure your weight in kilograms')


def workout_duration_mt_300(num):
    if num > 300:
        raise ValidationError('That`s impressive, but please take it easier with the workouts')
