from django import forms

from project_project.sport_app.models import Workout, CustomExercise, Article, CustomGoal


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['heading', 'category', 'abstract', 'body', 'article_image' ]
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A Nice Article Heading'
            }),
            'category': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }
            ),
            'abstract': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short summary of what the article is about'
            }
            ),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type the text of your article here'
            }
            ),
            'article_image': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.image.url'
            }
            )
        }
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'exercises', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={
                'size':'50',
                'title': 'Workout name:',
                'class': 'form-control'
                }),
            # TODO: INLINE FORMSET HERE!!!!
            'exercises': forms.SelectMultiple(
                attrs={
                    'size': '12',
                    'class': 'form-control'
                }
            ),
            'duration': forms.NumberInput(
                attrs={
                    'placeholder': '---',
                    'class': 'form-control'
                })
        }

class CustomGoalForm(forms.ModelForm):
    class Meta:
        model = CustomGoal
        fields = ['goal_name', 'is_accomplished', 'description']
        widget = {
            'goal_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'goal name'
                },
            ),
            'is_accomplished': forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                },
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your plan how you want to achieve this goal'
                },
            )
        }


class CustomExerciseForm(forms.ModelForm):
    class Meta:
        model = CustomExercise
        fields = ['name', 'type', 'body_parts',
                  'exercise_photo', 'metric', 'quantity']
        widgets = {
            'name': forms.TextInput(
             attrs={
                'class':'form-control',
                'placeholder': 'My Exercise'
             }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'metric': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'quantity': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0'
                }
            ),
            'exercise_photo': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'https://www.image.url/'
                }
            ),
            'body_parts': forms.SelectMultiple(
                attrs={
                    'size': '9',
                    'class': 'form-control'
                }
            )
        }