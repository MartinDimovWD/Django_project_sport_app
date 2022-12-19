import re

from django import forms
from django.forms import ModelForm, HiddenInput

from project_project.profiles.models import TraineeProfile, TrainerProfile
from project_project.sport_app.models import Goal


class TraineeProfileUpdateForm(forms.ModelForm):
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


class TrainerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ['training_field', 'years_experience', 'bio', 'phone_number', 'prime_membership']
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
                    'placeholder': '+359-xxx-xxx-xxx',
                }),
            'prime_membership': forms.CheckboxInput(
            )
        }


class CompleteTrainerProfileForm(ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ('client_type', 'profile', 'training_field','years_experience','sports','bio','phone_number')
        widgets = {'profile': HiddenInput(),
                   'client_type': HiddenInput(),
                   'training_field': forms.Select(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'years_experience': forms.NumberInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'sports': forms.SelectMultiple(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '--',
                        }),
                    'phone_number': forms.NumberInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '+359-xxx-xxx-xxx',
                        }),
                    'bio': forms.Textarea(
                        attrs={
                            'class': 'form-control',
                            'placeholder': 'Include any relevant professional experience. You can include certifications, testimonials, etc.',
                        })

                }

    def clean(self):
        super(CompleteTrainerProfileForm, self).clean()
        phone_number = int(self.cleaned_data.get('phone_number'))
        if len(str(phone_number))!=10:
            self._errors['phone_number'] = self.error_class([
                'Please enter a valid phone number. It should not start with 0! +359 is added automatically. It should be 10 digits long'
            ])
        print(len(str(phone_number)))
        return self.cleaned_data


class CompleteTraineeProfileForm(ModelForm):
    class Meta:
        model = TraineeProfile
        fields = ('client_type', 'profile', 'height','weight','experience','goals')
        widgets = {'profile': HiddenInput(),
                   'client_type': HiddenInput(),
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
                           'placeholder': '---',
                       }),
                   'goals': forms.SelectMultiple(
                       attrs={
                           'class': 'form-control',
                           'placeholder': '---',
                       })
                   }

    def __init__(self,*args,**kwargs):
        super(CompleteTraineeProfileForm,self).__init__(*args,**kwargs)
        self.fields['goals'].queryset = Goal.objects.filter(base_goal=True)

    def clean(self):
        super(CompleteTraineeProfileForm, self).clean()
        height = int(self.cleaned_data.get('height'))
        weight = int(self.cleaned_data.get('weight'))

        if 50>height or height>250:
            self._errors['height'] = self.error_class([
                'This height is very unlikely. Please note it is in centimeters!'
            ])
        if 30>weight or weight>250:
            self._errors['weight'] = self.error_class([
                'This weight is very unlikely. Please note it is in kilograms!'
            ])
        return self.cleaned_data

class ManagePrimeSubscriptionForm(ModelForm):
    class Meta:
        model = TrainerProfile
        fields = ('prime_membership',)
        widgets={
            'prime_membership': forms.CheckboxInput(

            )
        }