from django import forms

from project_project.sport_app.models import Exercise
from project_project.web_app.models import Rating, ExerciseRating, GymRating, TrainerRating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields=['rating', 'comment']
        widgets={
            'rating': forms.RadioSelect(
                attrs={
                    'default': '1'
                    # 'class': 'form-control',
                }
            ),
            'comment': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class ExerciseRatingForm(RatingForm):
    class Meta(RatingForm.Meta):
        model = ExerciseRating
        fields = ['rating', 'comment']


class GymRatingForm(RatingForm):
    class Meta(RatingForm.Meta):
        model = GymRating
        fields = ['rating', 'comment']


class TrainerRatingForm(RatingForm):
    class Meta(RatingForm.Meta):
        model = TrainerRating
        fields = ['rating', 'comment']


