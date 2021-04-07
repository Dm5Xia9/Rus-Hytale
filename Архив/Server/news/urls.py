from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/<int:new_id>/', views.deatail, name = 'deatail')
]