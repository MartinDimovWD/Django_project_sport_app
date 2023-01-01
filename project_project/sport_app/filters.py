import django_filters

from project_project.sport_app.models import Article


class ArticleCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {'category': ['exact']}


