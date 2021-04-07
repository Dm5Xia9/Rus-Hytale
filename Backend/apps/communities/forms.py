from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import communiti
from django.core.exceptions import ValidationError
class communiti_createForm(forms.Form):
     title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Название'}))
     Description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Описание'}))
     def clean_ava(self):
          ava = self.cleaned_data.get('ava')
          print(ava.url)
          if ava == None:
               raise ValidationError("Баг на мясокомбинате")
          return ava
     def save(self, commit=True):
          communiti_new = communiti(
               title = self.cleaned_data['title'],
               Description = self.cleaned_data['Description']
          )
          return communiti_new