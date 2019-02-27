from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView): 
    template_name = 'articles/article_create.html'  
    form_class = ArticleModelForm
    queryset = Article.objects.all() 
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
        # this will allow me to see what data is coming through the form

    # def get_success_url(self):
    #     return '/'

class ArticleListView(ListView): # this class inherits from ListView
    template_name = 'articles/article_list.html'  # this is one way to reference a template

    # it requires to provide a queryset
    queryset = Article.objects.all() # this is going to look for <blog>/<modelname>_list.html

class ArticleDetailView(DetailView): # this class inherits from ListView
    template_name = 'articles/article_detail.html'  # this is one way to reference a template
    # queryset = Article.objects.all() 
    # here I don't need a queryset. It still works fine without it.
    # this queryset actually limits the choices available for that DetailView (using filter)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView): 
    template_name = 'articles/article_create.html'  
    form_class = ArticleModelForm
    queryset = Article.objects.all() 
    # success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView): 
    template_name = 'articles/article_delete.html' 
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

    