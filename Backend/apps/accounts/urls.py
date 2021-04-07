from django.urls import path
from . import views, GETviews
from django.contrib.auth import views as authViews
app_name = 'accounts'
urlpatterns = [
     path('registration/', views.register, name='reg'),
     path('logout/', authViews.LogoutView.as_view(next_page='/'), name='logout'),
     path('login/', views.auth, name='login'),
     path('settings/', views.settings, name = 'settings'),
     path('accounts/<identifier>/', views.prof, name = 'prof'),
     path('accounts/', GETviews.accs, name = 'accs'),
]
