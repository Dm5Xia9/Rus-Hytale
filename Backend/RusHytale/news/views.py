from django.shortcuts import render

from .models import New


def index(request):
     latest_new_list = New.objects.all()[:3]
     if len(latest_new_list) == 1:
          return render(request, 'indexBase.html', {'num': 1, 'cont1': latest_new_list[0]})
     elif len(latest_new_list) == 2:
          return render(request, 'indexBase.html', {'num': 2, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1]})
     elif len(latest_new_list) == 3:
          return render(request, 'indexBase.html', {'num': 3, 'cont1': latest_new_list[0], 'cont2': latest_new_list[1], 'cont3': latest_new_list[2]})
     else:
          return render(request, 'indexBase.html', {'num': 0})
