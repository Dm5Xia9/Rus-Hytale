from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class articleCreateForm(forms.Form):
     content = forms.CharField( label='')
