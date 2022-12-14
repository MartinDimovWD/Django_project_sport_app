from django.urls import path, include

from project_project.sport_app.views import ArticlesListView, ArticleDetails, TrainersListView, TrainerDetails, \
    ExercisesListView, ExerciseDetails, WorkoutsListView, WorkoutDetails, WorkoutCreateView, WorkoutUpdateView, \
    WorkoutDeleteView, filter_exercises_by_bodypart, filter_articles_by_category, ArticleCreate, CustomExerciseCreate, \
    CustomExerciseUpdate, CustomExerciseDetail, CustomExerciseDelete, CustomExerciseList, CustomGoalCreate

urlpatterns=[
    path('articles/', include([
        path('', ArticlesListView.as_view(), name='articles list'),
        path('filter/<category>/', filter_articles_by_category, name='articles filter'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('article/<int:pk>', ArticleDetails.as_view(), name='article details'),
        path('create', ArticleCreate.as_view(), name='article create'),
    ])),
    path('trainers/',include([
        path('', TrainersListView.as_view(), name='trainers list'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('trainer/<int:pk>', TrainerDetails.as_view(), name='trainer details'),
    ])),
    path('exercises/',include([
        path('', ExercisesListView.as_view(), name='exercises list'),
        path('filter/<bodypart>', filter_exercises_by_bodypart, name='exercises filter'),
        # TODO: PUT A SLUG INSTEAD OF PK!
        path('exercise/<int:pk>', ExerciseDetails.as_view(), name='exercise details'),
        # path('exercise/fave/<int:pk>', add_to_favourites, name='add to fave'),
        path('custom/', include([
            path('', CustomExerciseList.as_view(), name='my exercises list'),
            path('create/', CustomExerciseCreate.as_view(), name='exercise create'),
            path('update/<int:pk>', CustomExerciseUpdate.as_view(), name='custom exercise update'),
            path('details/<int:pk>', CustomExerciseDetail.as_view(), name='custom exercise details'),
            path('delete/<int:pk>', CustomExerciseDelete.as_view(), name='custom exercise delete'),
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
    path('content/create-goal', CustomGoalCreate.as_view(), name='create custom goal')
]