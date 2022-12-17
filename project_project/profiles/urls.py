from django.urls import include, path

from project_project.accounts.views import UpdatePersonalView
from project_project.profiles.views import complete_trainer_profile_view, complete_trainee_profile_view, \
    UpdateTrainerProfileView, UpdateTraineeProfileView, TrainerProfileView, TraineeProfileView, TraineeDeleteView, \
    TrainerPersonalProfileView, TrainerDeleteView, ManagePrimeSubscriptionView

urlpatterns = [
    path('trainer/', include([
        path('complete-profile/', complete_trainer_profile_view, name='trainer complete profile'),
        path('update-profile/<int:pk>/', UpdateTrainerProfileView.as_view(), name='trainer update profile'),
        path('profile-details/<int:pk>/', TrainerProfileView.as_view(), name='trainer details'),
        path('profile-details/<int:pk>/trainer', TrainerPersonalProfileView.as_view(), name='trainer profile details'),
        path('profile-delete/<int:pk>/', TrainerDeleteView.as_view(), name='trainer profile delete'),
        path('manage-prime/<int:pk>', ManagePrimeSubscriptionView.as_view(), name='manage prime'),

    ])),
    path('trainee/', include([
        path('complete-profile/', complete_trainee_profile_view, name='trainee complete profile'),
        path('update-profile/<int:pk>/', UpdateTraineeProfileView.as_view(), name='trainee update profile'),
        path('profile-details/<int:pk>/', TraineeProfileView.as_view(), name='trainee profile details'),
        path('profile-delete/<int:pk>/', TraineeDeleteView.as_view(), name='trainee profile delete')
    ]))
]

