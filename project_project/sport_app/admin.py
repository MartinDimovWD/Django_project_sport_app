from django.contrib import admin

from project_project.sport_app.models import CustomGoal, CustomExercise, Sport, Goal, Article, Exercise, Workout


# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_parts', 'type', 'metric',]
    list_filter = ['name', 'body_parts', 'type']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['heading', 'author', 'publication_date', 'category']
    list_filter = ['category', 'author', 'publication_date']

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomExercise)
class CustomExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_parts', 'type', 'metric', 'owner' ]
    list_filter = ['name', 'body_parts', 'type', 'owner']

