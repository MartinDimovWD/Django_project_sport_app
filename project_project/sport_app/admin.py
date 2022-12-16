from django.contrib import admin

from project_project.sport_app.models import CustomGoal, CustomExercise, Sport, Goal, Article, Exercise, Workout


# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_parts', 'type', 'metric',]
    list_filter = ['name', 'body_parts', 'type']
    list_display_links = []
    list_editable = []
    search_fields = ['name','type','body_parts']
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['heading', 'author', 'publication_date', 'category']
    list_filter = ['category', 'author', 'publication_date']
    list_display_links = []
    list_editable = []
    search_fields = ['heading', 'category', 'body', 'abstract']
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['goal_name','base_goal']
    list_filter = ['base_goal']
    list_display_links = []
    list_editable = []
    search_fields = ['goal_name']

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ['sport_name']
    list_filter = ['is_group_sport']
    list_display_links = []
    list_editable = []
    search_fields = ['sport_name']

@admin.register(CustomExercise)
class CustomExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'body_parts', 'type', 'metric', 'owner' ]
    list_filter = ['name', 'body_parts', 'type', 'owner']
    list_display_links = []
    list_editable = []
    search_fields = ['name', 'body_parts', 'type']
