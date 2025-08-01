from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.Lista_posts.html, name='Lista_Posts.html'),
]