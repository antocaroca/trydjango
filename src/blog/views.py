from django.shortcuts import render

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    DeleteView
)

from .models import Article

class ArticleListView(ListView): # this class inherits from ListView
    template_name = 'articles/article_list.html'  # this is one way to reference a template

    # it requires to provide a queryset
    queryset = Article.objects.all() # this is going to look for <blog>/<modelname>_list.html