from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput

from project_project.accounts.models import AppUser
from project_project.web_app.field_validators import age_validator


class ClientSignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('email', 'username', 'first_name', 'last_name', 'gender', 'age', 'location', 'password1', 'password2', 'profile_picture')
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email@any.com'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'myname'
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
            'password1': forms.HiddenInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '********'
                }
            ),
            'password2': forms.HiddenInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '********'
                }
            ),
            'profile_picture': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://www.image.url'
                }
            ),
        }

    def clean(self):
        super(ClientSignUpForm, self).clean()
        age = int(self.cleaned_data.get('age'))
        if age>120:
            print(age)
            self._errors['age'] = self.error_class([
                'You are too old. You should be taking a break'
            ])
        return self.cleaned_data


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


# class SignInForm(forms.ModelForm):
#     class Meta:
#         model = AppUser
#         fields = []
#         widgets = {
#             'email': forms.EmailInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Enter your email'
#                 }
#             )
#         }