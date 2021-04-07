from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'communities'
urlpatterns = [
    path('communities/', views.communities, name = 'communities'),
    path('communities/add/', views.communiti_create, name = 'communities_add'),
    path('communities/<communiti_identifier>/', views.communiti, name = 'communiti_c'),
]