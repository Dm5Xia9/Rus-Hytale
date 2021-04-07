from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import new
def index(request):
    latest_new_list = new.objects.all()[:3]
    if len(latest_new_list) == 1:
        return render(request, 'news/list.html', {'num': 1,'cont1': latest_new_list[0], 'img1' : "бубубе"})
    elif len(latest_new_list) == 2:
        return render(request, 'news/list.html', {'num': 2, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1]})
    elif len(latest_new_list) == 3:
        return render(request, 'news/list.html', {'num': 3, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1], 'cont3' : latest_new_list[2]})
    else:
        return render(request, 'news/list.html', {'num': 0})
def deatail(request, new_id):
    latest_new = new.objects.get( id = new_id)
    return render(request, 'news/blogNewConfig.html', {'latest_new': latest_new})