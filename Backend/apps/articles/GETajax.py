from .models import article, Like, Delike
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from . import Checks
def minusLike(request, article_object):
     Like.objects.get(user=request.user, article=article_object).delete()
     article_object.likes -= 1
     article_object.save()
def plusLike(request, article_object):
     like_object = Like(user=request.user, article=article_object)
     like_object.article.likes += 1
     like_object.article.save()
     like_object.save()
def minusDilike(request, article_object):
     Delike.objects.get(user=request.user, article=article_object).delete()
     article_object.dilikes -= 1
     article_object.save()
def plusDilike(request, article_object):
     dilike_object = Delike(user=request.user, article=article_object)
     dilike_object.article.dilikes += 1
     dilike_object.article.save()
     dilike_object.save()
@csrf_exempt
def like(request):
    if request.method == 'GET' and request.user.is_authenticated: #юзается метод GET и пользователь авторизован
          id_article = Checks.IntorNone(request.GET.get("id_article", ''), None)
          if id_article is not None: #данные валидны
               article_object = article.objects.get(id=id_article)
               like_bool = not Checks.likeBoolCheck(request, article_object)
               if like_bool:#лайк уже был поставлен
                    minusLike(request, article_object)
                    return HttpResponse(f"- {article_object.likes} {article_object.dilikes}")
               else: #лайк не был поставлен
                    dilike_bool = not Checks.dilikeBoolCheck(request, article_object)
                    if dilike_bool: #дизлайк был поставлен
                         minusDilike(request, article_object)
                         plusLike(request, article_object)
                         return HttpResponse(f"* {article_object.likes} {article_object.dilikes}")
                    else: # дизлайк не был поставлен
                         plusLike(request, article_object)
                         return HttpResponse(f"+ {article_object.likes} {article_object.dilikes}")
          else: #данные не валидны
               return HttpResponse("Не хороший!")
    else: #Не юзается Get или пользователь не авторизован
          return HttpResponse("Не хороший!")
@csrf_exempt
def dilike(request):
    if request.method == 'GET' and request.user.is_authenticated:
          id_article = Checks.IntorNone(request.GET.get("id_article", ''), None)
          if id_article is not None:
               article_object = article.objects.get(id=id_article)
               dilike_bool = not Checks.dilikeBoolCheck(request, article_object)
               if dilike_bool:
                    minusDilike(request, article_object)
                    return HttpResponse(f"- {article_object.likes} {article_object.dilikes}")
               else:
                    like_bool = not Checks.likeBoolCheck(request, article_object)
                    if like_bool:
                         minusLike(request, article_object)
                         plusDilike(request, article_object)
                         return HttpResponse(f"* {article_object.likes} {article_object.dilikes}")
                    else:
                         plusDilike(request, article_object)
                         return HttpResponse(f"+ {article_object.likes} {article_object.dilikes}")
          else:
               return HttpResponse("Не хороший!")
    else:
         return HttpResponse("Не хороший!")