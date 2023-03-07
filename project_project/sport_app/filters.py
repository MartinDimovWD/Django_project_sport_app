import django_filters

from project_project.sport_app.models import Article, Exercise


class ArticleCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {'category': ['exact']}


class ExerciseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Exercise
        fields = ['body_parts', 'type']
