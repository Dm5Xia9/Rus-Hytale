from django.shortcuts import render
from .models import New, views_new
from django.core.exceptions import ObjectDoesNotExist
from . import Checks
from Support import get_or_none
TEMP_DIR = "news/"
def addViews(request, answer_id):
     try:
          views_new.objects.get(user=request.user, new=answer_id)
     except ObjectDoesNotExist:
          view_object = views_new(user=request.user, new=answer_id)
          view_object.save()
          answer_id.views += 1
          answer_id.save()
def search_id(request):
     answer_id = Checks.checking_id(request.GET.get("id", None))
     if answer_id is not None: #В Get_id норм id
          if request.user.is_authenticated: #Я авторизован
               latest_new = get_or_none(New, id=answer_id.id)
               communiti_ones = request.user.communiti_set.all()
               like_bool = Checks.likeBoolCheck(request, answer_id.id)
               dilike_bool = Checks.dilikeBoolCheck(request, answer_id.id)
               if latest_new is not None:
                    if len(communiti_ones) == 1:
                         return render(request, TEMP_DIR + 'new.html', {'latest': latest_new, 'communiti_c': True,
                                                                        "new_like": like_bool,
                                                                        "new_dilike": dilike_bool, })
                    elif len(communiti_ones) == 0:
                         return render(request, TEMP_DIR + 'new.html', {'latest': latest_new, 'communiti_c': False})
               else:
                    return render(request, 'Errors/404.html')
          else: #Не авторизован
               latest_new = get_or_none(New, id=answer_id.id)
               return render(request, TEMP_DIR + 'new.html', {'latest': latest_new, 'communiti_c': False})
     else: #В Get_id печаль
          return render(request, 'Errors/404.html')
def search_communiti_id(request):
     answer_communiti_id = Checks.checking_communiti_id(request.GET.get("communiti_id", None))
     if answer_communiti_id is not None:
          if request.user.is_authenticated:
               communiti_news = New.objects.filter(communiti = answer_communiti_id)[::-1]
               communiti_ones = request.user.communiti_set.all()
               if len(communiti_ones) == 1:
                    return render(request, TEMP_DIR + 'news.html',
                                  {'latest_news': communiti_news, 'communiti_c': True, 'tg_id':answer_communiti_id.id})
               elif len(communiti_ones) == 0:
                    return render(request, TEMP_DIR + 'news.html', {'latest_news': communiti_news, 'communiti_c': False, 'tg_id':answer_communiti_id.id})
               else:
                    return render(request, TEMP_DIR + 'news.html', {'latest_news': communiti_news, 'communiti_c': False, 'tg_id':answer_communiti_id.id})
          else:
               communiti_news = New.objects.filter(communiti=answer_communiti_id)[::-1]
               return render(request, TEMP_DIR + 'news.html',
                             {'latest_news': communiti_news, 'communiti_c': False, 'tg_id': answer_communiti_id.id})
     else:
          return render(request, 'Errors/404.html')