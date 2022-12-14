from django import forms
from django.forms import ModelForm

from project_project.profiles.models import TraineeProfile, TrainerProfile
from project_project.sport_app.models import Goal


class TraineeProfileForm(forms.ModelForm):
    class Meta:
        model = TraineeProfile
        fields = ['height', 'weight', 'experience', 'goals']
        widgets = {
            'height': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '---',
                }),
            'weight': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '---',
                }),
            'experience': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'goals': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                })
        }


class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['training_field', 'years_experience', 'bio', 'phone_number']
        widgets = {
            'training_field': forms.Select(
                attrs={
                    'class': 'form-control',
                }),
            'years_experience': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '--',
                }),
            'bio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '--',
                }),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'xxx-xxx-xxx',
                })
        }


# class CompleteTrainerProfileForm(forms.ModelForm):
#     class Meta:
#         model = TrainerProfile
#         fields = ('client_type', 'profile', 'training_field','years_experience','sports','bio','phone_number')
#         widgets = {
#             'training_field': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '--',
#                 }),
#             'years_experience': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '--',
#                 }),
#             'sports': forms.SelectMultiple(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '--',
#                 }),
#             'phone_number': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'xxx-xxx-xxx',
#                 }),
#             'bio': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Include any relevant professional experience. You can include certifications, testimonials, etc.',
#                 })
#
#         }