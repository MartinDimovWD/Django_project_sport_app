from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from project_project.profiles.mixins import TrainerProfileRequiredMixin, PrimeRequiredMixin
from project_project.sport_app.forms import ArticleForm
from project_project.sport_app.models import Article, UserReadingList


class ArticlesListView(ListView):
    template_name = 'content/articles/articles-list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 6
    # queryset = Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Article.objects.all()) == 2:
            context['featured'] = Article.objects.all()[0]
            context['featured2'] = Article.objects.all()[1]
        # context['form'] = self.filterset.form
        # TODO: might put featured articles instead of the first 3
        reading_list = [art.article for art in UserReadingList.objects.filter(user=self.request.user)]
        context['reading_list'] = reading_list
        return context

    def get_queryset(self):
        articles = Article.objects.order_by('-publication_date')
        return articles


class ArticleDetails(DetailView):
    template_name = 'content/articles/article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        reading_list = [art.article for art in UserReadingList.objects.filter(user=self.request.user)]
        context['reading_list'] = reading_list
        return context


class ArticleCreate(TrainerProfileRequiredMixin, PrimeRequiredMixin, CreateView):
    template_name = 'content/articles/create-article.html'
    form_class = ArticleForm
    # model = Article
    # fields = ['heading', 'abstract', 'body', 'article_image', 'category']
    context_object_name = 'article'
    success_url = reverse_lazy('articles list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def add_article_to_reading_list(request, pk):
    article = Article.objects.get(pk=pk)
    article_in_reading_list = UserReadingList.objects.filter(article=article, user=request.user)
    if article_in_reading_list:
        article_in_reading_list.delete()
    else:
        UserReadingList.objects.create(article=article, user=request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
