from django.urls import path 
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView
)

app_name = 'articles'
urlpatterns = [
     path('', ArticleListView.as_view(), name='article-list'),
     path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
     path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
     path('create/', ArticleCreateView.as_view(), name='article-create'),
]