from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
     path('auth/', views.auth, name='auth'),
     path('registration/', views.SignUpView.as_view(), name='reg'),
]
