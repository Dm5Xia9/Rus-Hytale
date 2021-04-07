from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/add/', views.news_add, name='news_add'),
    path('news/like/', views.like),
    path('news/dilike/', views.dilike),
    path('news/file/', views.file),
]