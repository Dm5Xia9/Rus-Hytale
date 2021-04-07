from django.urls import path
from . import views, GETajax, POSTajax
from django.conf.urls import url
app_name = 'articles'
urlpatterns = [
    path('articles/', views.articles, name = 'articles'),
    path('articles/add/', views.articles_add, name = 'articles_add'),
    path('articles/tag_add/', views.articles_tag_add, name = 'articles_tag_add'),
    path('articles/tag_list/', views.tag_list, name = 'tag_list'),
    path('articles/like/', GETajax.like),
    path('articles/dilike/', GETajax.dilike),
    path('articles/file/', POSTajax.file),
]