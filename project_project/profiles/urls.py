from django.urls import include, path

from project_project.accounts.views import UpdatePersonalView
from project_project.profiles.views import complete_trainer_profile_view, complete_trainee_profile_view, \
    UpdateTrainerProfileView, UpdateTraineeProfileView, TrainerProfileView, TraineeProfileView, TraineeDeleteView, \
    TrainerPersonalProfileView, TrainerDeleteView, ManagePrimeSubscriptionView, hire_coach_view

urlpatterns = [
    path('trainer/', include([
        path('complete-profile/', complete_trainer_profile_view, name='trainer complete profile'),
        path('update-profile/<slug:slug>/', UpdateTrainerProfileView.as_view(), name='trainer update profile'),
        # path('profile-details/<int:pk>/', TrainerProfileView.as_view(), name='trainer details'),
        path('profile-details/<slug:slug>/trainer', TrainerPersonalProfileView.as_view(), name='trainer profile details'),
        path('profile-delete/<slug:slug>/', TrainerDeleteView.as_view(), name='trainer profile delete'),
        path('manage-prime/<slug:slug>', ManagePrimeSubscriptionView.as_view(), name='manage prime'),

    ])),
    path('trainee/', include([
        path('complete-profile/', complete_trainee_profile_view, name='trainee complete profile'),
        path('update-profile/<slug:slug>/', UpdateTraineeProfileView.as_view(), name='trainee update profile'),
        path('profile-details/<slug:slug>/', TraineeProfileView.as_view(), name='trainee profile details'),
        path('profile-delete/<slug:slug>/', TraineeDeleteView.as_view(), name='trainee profile delete')
    ])),
    path('hire-coach/<int:coach_pk>', hire_coach_view, name='hire coach'),
]

