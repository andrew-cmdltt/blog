
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from posts.models import Post
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.PostController.showPost, name='post'),
    path('add/', views.PostController.addPost, name='add'),
    url(r'^edit/(?P<pk>\d+)$', views.PostController.editPost, name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PostController.deletePost, name='delete'),
   ]




