from django.urls import path
from .views import(
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'), # .as_view turns it into a function based view
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
]