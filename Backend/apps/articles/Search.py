from django.shortcuts import render
from .models import article, views_article, articles_tag
from django.core.exceptions import ObjectDoesNotExist
from . import Checks
TEMP_DIR = "articles/"
def addViews(request, answer_id):
     try:
          views_article.objects.get(user=request.user, article=answer_id)
     except ObjectDoesNotExist:
          view_object = views_article(user=request.user, article=answer_id)
          view_object.save()
          answer_id.views += 1
          answer_id.save()
def search_id(request):
     answer_id = Checks.checking_id(request.GET.get("id", None))
     if answer_id is not None: #В Get_id норм id
          if request.user.is_authenticated: #Я авторизован
               addViews(request, answer_id)
               like_bool = Checks.likeBoolCheck(request, answer_id)
               dilike_bool = Checks.dilikeBoolCheck(request, answer_id)
               return render(request, TEMP_DIR + 'article.html',
                                  {"article": answer_id,
                                   "article_like": like_bool,
                                   "article_dilike": dilike_bool, "det":1})
          else: #Не авторизован
               return render(request, TEMP_DIR + 'article.html', {"article": answer_id})
     else: #В Get_id печаль
          return render(request, 'Errors/404.html')
def search_tag_id(request):
     answer_tag_id = Checks.checking_tag_id(request.GET.get("tag_id", None))
     if answer_tag_id is not None: #В Get_tag_id норм id
          articles = []
          ars_tag = articles_tag.objects.filter(tag = answer_tag_id)
          print(ars_tag)
          if(len(ars_tag) < 10):
               ars_tag = ars_tag[::-1]
               print(ars_tag)
          else:
               ars_tag = ars_tag[len(articles_tag.objects.all()) - 10::-1]
          for ar_tag in ars_tag:
               articles.append(ar_tag.article)

          return render(request, TEMP_DIR + 'articles.html',
                             {"articles": articles, "tg_id":answer_tag_id.id})
     else:
          return render(request, 'Errors/404.html')
def search_user_id(request):
     answer_tag_id = Checks.checking_user_id(request.GET.get("user_id", None))
     if answer_tag_id is not None:
          articles = article.objects.filter(user = answer_tag_id)[::-1]

          return render(request, TEMP_DIR + 'articles.html',
                             {"articles": articles})
     else:
          return render(request, 'Errors/404.html')