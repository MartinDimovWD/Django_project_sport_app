from django.core.exceptions import ValidationError


# acc
def name_alpha_validator(name):
    pass


def age_validator(age):
    if age>=18:
        return age
    else:
        print(age)
        raise ValidationError('Too young, mate')


# profile
def phone_number_validator(number):
    pass

