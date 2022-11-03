from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetail, AddPost, EditPost, DeletePost


urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetail.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/edit/<int:pk>', EditPost.as_view(), name='edit-post'),
    path('article/<int:pk>/remove', DeletePost.as_view(), name='delete-post')
]
