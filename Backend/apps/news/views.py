from django.shortcuts import render, redirect
from .models import New
from Support import get_or_none
from RusHytale.settings import ALLOWED_HOSTS
from . import Search
TEMP_DIR = "news/"

def news(request):
     if request.GET != {}:
          for get in request.GET:
               if get == 'id':
                    return Search.search_id(request)
               elif get == 'communiti_id':
                    return Search.search_communiti_id(request)
               else:
                    return render(request, 'Errors/404.html')
     else:
          if request.user.is_authenticated:
               latest_news = New.objects.all()
               latest_news = latest_news[::-1]
               communiti_ones = request.user.communiti_set.all()
               if len(communiti_ones) == 1:
                    return render(request, TEMP_DIR + 'news.html',
                                  {'latest_news': latest_news, 'communiti_c': True, "general":True})
               elif len(communiti_ones) == 0:
                    return render(request, TEMP_DIR + 'news.html', {'latest_news': latest_news, 'communiti_c': False, "general":True})
               else:
                    return render(request, TEMP_DIR + 'news.html', {'latest_news': latest_news, 'communiti_c': False, "general":True})
          else:
               latest_news = New.objects.all()
               latest_news = latest_news[::-1]
               return render(request, TEMP_DIR + 'news.html',
                             {'latest_news': latest_news, 'communiti_c': False, "general": True})

from bs4 import BeautifulSoup
def news_add(request):
     if request.user.is_authenticated:
          communiti_ones = request.user.communiti_set.all()
          if len(communiti_ones) == 1:
               if request.method == 'POST':
                    soup = BeautifulSoup(request.POST.get('content'), "lxml")
                    cover = ''.join(str(x) for x in soup.find_all('p')[:2])
                    new_new = New(communiti=communiti_ones[0], title=request.POST.get('title'),
                                          text=request.POST.get('content'), text_mini=cover)
                    new_new.save()
                    return redirect(f'/news/?id={new_new.id}')
               else:
                    return render(request, TEMP_DIR + 'new_create.html')
          else:
               return render(request, 'Errors/404.html')
     else:
          return render(request, 'Errors/404.html')
from django.shortcuts import render
from .models import  new_image
from .models import  Like_new as Like
from .models import  Delike_new as Delike
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import Checks
@csrf_exempt
def file(request):
     if request.method == "POST":
          try:
               im = new_image(image=request.FILES.get('file'))
               im.save()
               return JsonResponse({'location': f'http://127.0.0.1:8000{im.image.url}'})
          except:
               return render(request, 'Errors/404.html')
     else:
          return render(request, 'Errors/404.html')
def minusLike(request, new_object):
     Like.objects.get(user=request.user, new=new_object).delete()
     new_object.likes -= 1
     new_object.save()
def plusLike(request, new_object):
     like_object = Like(user=request.user, new=new_object)
     like_object.new.likes += 1
     like_object.new.save()
     like_object.save()
def minusDilike(request, new_object):
     Delike.objects.get(user=request.user, new=new_object).delete()
     new_object.dilikes -= 1
     new_object.save()
def plusDilike(request, new_object):
     dilike_object = Delike(user=request.user, new=new_object)
     dilike_object.new.dilikes += 1
     dilike_object.new.save()
     dilike_object.save()
@csrf_exempt
def like(request):
    if request.method == 'GET' and request.user.is_authenticated: #юзается метод GET и пользователь авторизован
          id_new = Checks.IntorNone(request.GET.get("id_new", ''), None)
          if id_new is not None: #данные валидны
               new_object = get_or_none(New, id = id_new)
               if new_object is not None:
                    like_bool = not Checks.likeBoolCheck(request, new_object)
                    if like_bool:#лайк уже был поставлен
                         minusLike(request, new_object)
                         return HttpResponse(f"- {new_object.likes} {new_object.dilikes}")
                    else: #лайк не был поставлен
                         dilike_bool = not Checks.dilikeBoolCheck(request, new_object)
                         if dilike_bool: #дизлайк был поставлен
                              minusDilike(request, new_object)
                              plusLike(request, new_object)
                              return HttpResponse(f"* {new_object.likes} {new_object.dilikes}")
                         else: # дизлайк не был поставлен
                              plusLike(request, new_object)
                              return HttpResponse(f"+ {new_object.likes} {new_object.dilikes}")
               else:
                    return HttpResponse("Не хороший!")
          else: #данные не валидны
               return HttpResponse("Не хороший!")
    else: #Не юзается Get или пользователь не авторизован
          return HttpResponse("Не хороший!")
@csrf_exempt
def dilike(request):
    if request.method == 'GET' and request.user.is_authenticated:
          id_new = Checks.IntorNone(request.GET.get("id_new", ''), None)
          if id_new is not None:
               new_object = get_or_none(New, id = id_new)
               if new_object is not None:
                    dilike_bool = not Checks.dilikeBoolCheck(request, new_object)
                    if dilike_bool:
                         minusDilike(request, new_object)
                         print(f"- {new_object.likes} {new_object.dilikes}")
                         return HttpResponse(f"- {new_object.likes} {new_object.dilikes}")
                    else:
                         like_bool = not Checks.likeBoolCheck(request, new_object)
                         if like_bool:
                              minusLike(request, new_object)
                              plusDilike(request, new_object)
                              print(f"- {new_object.likes} {new_object.dilikes}")
                              return HttpResponse(f"* {new_object.likes} {new_object.dilikes}")
                         else:
                              plusDilike(request, new_object)
                              print(f"- {new_object.likes} {new_object.dilikes}")
                              return HttpResponse(f"+ {new_object.likes} {new_object.dilikes}")
               else:
                    return HttpResponse("Не хороший!")
          else:
               return HttpResponse("Не хороший!")
    else:
         return HttpResponse("Не хороший!")
def e_handler404(request, exception):
     return render(request, 'Errors/404.html')
