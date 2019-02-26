from django.urls import path
from .views import(
    ArticleListView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'), # .as_view turns it into a function based view
]