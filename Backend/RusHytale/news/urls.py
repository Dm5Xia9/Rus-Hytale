from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('news', views.news, name='news'),
    path('news/<int:new_id>/', views.deatail, name = 'deatail'),
]