from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetail, AddPost


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]
