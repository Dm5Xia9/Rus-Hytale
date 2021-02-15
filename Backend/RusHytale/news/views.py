from django.shortcuts import render
from django.template import RequestContext
from .models import New


def index(request):
     latest_new_list = New.objects.all()[:3]
     if len(latest_new_list) == 1:
          return render(request, 'Config/index.html', {'num': 1, 'cont1': latest_new_list[0]})
     elif len(latest_new_list) == 2:
          return render(request, 'Config/index.html', {'num': 2, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1]})
     elif len(latest_new_list) == 3:
          return render(request, 'Config/index.html', {'num': 3, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1], 'cont3': latest_new_list[2]})
     else:
          return render(request, 'Config/index.html', {'num': 0})
def deatail(request, new_id):
    latest_new = New.objects.get( id = new_id)
    return render(request, 'Config/new.html', {'latest_new': latest_new})
def news(request):
     latest_news = New.objects.all()
     latest_news = latest_news[::-1]
     return render(request, 'Config/news.html', {'latest_news': latest_news})



def e_handler404(request, exception):
     return render(request, 'Config/404.html')
