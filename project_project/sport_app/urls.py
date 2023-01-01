from django.urls import path, include

from project_project.sport_app.views.articles_views import ArticlesListView, ArticleDetails, ArticleCreate
from project_project.sport_app.views.exercises_views import ExercisesListView, ExerciseDetails, CustomExerciseList, \
    CustomExerciseCreate, CustomExerciseUpdate, CustomExerciseDetail, CustomExerciseDelete
from project_project.sport_app.views.goal_views import CustomGoalCreate, manage_goals
from project_project.sport_app.views.filtering_views import filter_exercises_by_bodypart, filter_articles_by_category, filter_trainers_by_location
from project_project.sport_app.views.trainers_views import TrainersListView, TrainerDetails
from project_project.sport_app.views.workouts_views import WorkoutsListView, WorkoutCreateView, WorkoutDetails, \
    WorkoutUpdateView, WorkoutDeleteView

urlpatterns=[
    path('articles/', include([
        path('', ArticlesListView.as_view(), name='articles list'),
        path('filter/<category>/', filter_articles_by_category, name='articles filter'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('article/<slug:slug>', ArticleDetails.as_view(), name='article details'),
        path('create', ArticleCreate.as_view(), name='article create'),
    ])),
    path('trainers/',include([
        path('', TrainersListView.as_view(), name='trainers list'),
        path('filter/<location>/', filter_trainers_by_location, name='trainers filter'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('trainer/<slug:slug>', TrainerDetails.as_view(), name='trainer details'),
    ])),
    path('exercises/',include([
        path('', ExercisesListView.as_view(), name='exercises list'),
        path('filter/<bodypart>', filter_exercises_by_bodypart, name='exercises filter'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('exercise/<slug:slug>', ExerciseDetails.as_view(), name='exercise details'),
        # path('exercise/fave/<int:pk>', add_to_favourites, name='add to fave'),
        path('custom/', include([
            path('', CustomExerciseList.as_view(), name='my exercises list'),
            path('create/', CustomExerciseCreate.as_view(), name='exercise create'),
            path('update/<slug:slug>', CustomExerciseUpdate.as_view(), name='custom exercise update'),
            path('details/<slug:slug>', CustomExerciseDetail.as_view(), name='custom exercise details'),
            path('delete/<slug:slug>', CustomExerciseDelete.as_view(), name='custom exercise delete'),
        ]))
    ])),
    path('workouts/',include([
        path('', WorkoutsListView.as_view(), name='workouts list'),
        # path('create-new-workout/', create_workout, name='workout create'),
        path('create-new-workout/', WorkoutCreateView.as_view(), name='workout create'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('workout/', include([
            path('<int:pk>', WorkoutDetails.as_view(), name='workout details'),
            path('<int:pk>/update', WorkoutUpdateView.as_view(), name='workout update'),
            path('<int:pk>/delete', WorkoutDeleteView.as_view(), name='workout delete'),
            ]))
    ])),
    path('content/create-goal', CustomGoalCreate.as_view(), name='create custom goal'),
    path('content/manage-goals', manage_goals, name='manage goals'),
]