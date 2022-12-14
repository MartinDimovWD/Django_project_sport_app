from django.urls import path, include

from project_project.accounts.views import TrainerSignUpView, TraineeSignUpView, SignInView, SignOutView, \
    combined_sign_up_view, UpdatePersonalView

urlpatterns = [
    path('accounts/', include([
        path('sign-up/', include([
            path('', combined_sign_up_view, name='combined register'),
            path('trainer/', TrainerSignUpView.as_view(), name='trainer sign up'),
            path('trainee/', TraineeSignUpView.as_view(), name='trainee sign up'),
        ])),
        path('login/', SignInView.as_view(), name='log in'),
        path('sign-out.html/', SignOutView.as_view(), name='sign out'),
        path('update-personal/<int:pk>', UpdatePersonalView.as_view(), name='user update personal'),

    ]))
]