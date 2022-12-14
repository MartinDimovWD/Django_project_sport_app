from django import forms
from django.forms import PasswordInput

from project_project.accounts.models import AppUser


class AppUserUpdateForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'username', 'location', 'profile_picture']
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email@any.com'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'myname',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Jon'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Doe'
                }
            ),
            'location': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '20'
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'profile_picture': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://www.image.url'
                }
            ),
        }

