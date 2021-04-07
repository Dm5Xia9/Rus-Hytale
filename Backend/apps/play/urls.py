from django.urls import path
from . import views
app_name = 'play'
urlpatterns = [
     path('play/', views.play, name='play'),
]