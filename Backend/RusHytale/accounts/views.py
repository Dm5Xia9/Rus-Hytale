from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
def auth(request):
     return render(request, 'Config/auth.html')

class SignUpView(generic.CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/reg.html'
def prof(request, identifier):
    AccSettModelDop = UserProfile.objects.get(identifier = identifier)
    AccSettModel = User.objects.get(id=AccSettModelDop.id)
    if request.method == "POST":
        AccSettModel.username = request.POST.get("username")
        AccSettModel.first_name = request.POST.get("first_name")
        AccSettModel.last_name = request.POST.get("last_name")
        AccSettModelDop.identifier = request.POST.get("identifier")
        AccSettModelDop.city = request.POST.get("city")
        AccSettModelDop.telephone = request.POST.get("telephone")
        AccSettModelDop.DateBirth = request.POST.get("DateBirth")
        AccSettModelDop.save()
        AccSettModel.save()
        return render(request, 'Config/AccSettings.html', {'UserDop': AccSettModelDop})
    else:
        return render(request, 'Config/AccSettings.html', {'UserDop': AccSettModelDop})
def settings(request):
    if request.user.is_authenticated:
        AccSettModel = User.objects.get(id=request.user.id)
        AccSettModelDop = UserProfile.objects.get(id=request.user.id)
        if request.method == "POST":
            AccSettModel.username = request.POST.get("username")
            AccSettModel.first_name = request.POST.get("first_name")
            AccSettModel.last_name = request.POST.get("last_name")
            AccSettModelDop.identifier = request.POST.get("identifier")
            AccSettModelDop.city = request.POST.get("city")
            AccSettModelDop.telephone = request.POST.get("telephone")
            AccSettModelDop.DateBirth = request.POST.get("DateBirth")
            AccSettModelDop.save()
            AccSettModel.save()
            return render(request, 'Config/AccSettings.html', {'UserDop': AccSettModelDop})
        else:
            return render(request, 'Config/AccSettings.html', {'UserDop': AccSettModelDop})
    else:
        return render(request, 'Config/404.html')