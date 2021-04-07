from django.shortcuts import render, redirect
from .models import article, tag_base, articles_tag
from . import Search
from accounts.models import tag_interest
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import Checks
from datetime import datetime
TEMP_DIR = "articles/"
@csrf_exempt
def articles(request):
     # if request.method == 'POST':
     #      if request.GET != {}:
     #           for get in request.GET:
     #                if get == 'id':
     #                     return Search.search_id(request)
     #                elif get == 'tag_id':
     #                     return Search.search_tag_id(request)
     #                elif get == 'user_id':
     #                     return Search.search_user_id(request)
     #                else:
     #                     return render(request, 'Errors/404.html')
     #      nm = int(request.POST.get('num_articles'))
     #      articles = article.objects.all()[::-1]
     #      print(len(articles))
     #      print(nm)
     #      articles = articles[nm:nm+10]
     #      PATTERN_OUT = "%Y.%m.%d"
     #      hfhfg = []
     #      for ar in articles:
     #           dt = datetime.strftime(ar.DateCreate, PATTERN_OUT)
     #           hfhfg.append({'avaurl': ar.user.avatar.url, 'acurl': "/accounts/"+ar.user.identifier+"/",
     #                                'usname': ar.user.username, 'date': dt,
     #                                'arturl':"/articles/?id="+ str(ar.id), 'artname':ar.title, 'v': ar.views, 'l': ar.likes,
     #                                'dl': ar.dilikes, 'content': ar.cover
     #                                })
     #      return JsonResponse({'arts': hfhfg})
     if request.GET != {}:
          for get in request.GET:
               if get == 'id':
                    return Search.search_id(request)
               elif get == 'tag_id':
                    return Search.search_tag_id(request)
               elif get == 'user_id':
                    return Search.search_user_id(request)
               else:
                    return render(request, 'Errors/404.html')
     else:
          articles = article.objects.all()[::-1]
          return render(request, TEMP_DIR + 'articles.html',
                        {"articles": articles, "general":True})
def articles_tag_add(request):
     return render(request, 'Errors/404.html')
from bs4 import BeautifulSoup
import simplejson
@csrf_exempt
def articles_add(request):
     if request.user.is_authenticated:
          popular_articles = article.objects.order_by("views")
          if request.method == 'POST':
               try:
                    my_tags_id = simplejson.loads(request.POST.get('data_tags'))
               except:
                    return render(request, 'Errors/404.html')
               soup = BeautifulSoup(request.POST.get('content'), "lxml")
               cover = ''.join(str(x) for x in soup.find_all('p')[:2])
               article_new = article(user = request.user, title = request.POST.get('title'), content = request.POST.get('content'), cover = cover)
               article_new.save()
               request.user.messages_count += 1
               request.user.save()
               for my_tag_id in my_tags_id:
                    try:
                         tag_base_my = tag_base.objects.get(id=my_tag_id)
                         articles_new_tag = articles_tag(tag=tag_base_my, article = article_new)
                         articles_new_tag.save()
                    except:
                         return render(request, 'Errors/404.html')
               return redirect(f'/articles/?id={article_new.id}')
          else:

               return render(request, TEMP_DIR + 'article_create.html',
                        { "popular_articles": popular_articles, 'tags_base':tag_base.objects.all()})
     else:
          return render(request, 'Errors/404.html')
@csrf_exempt
def tag_list(request):
     if request.user.is_authenticated:
          if(request.method == 'POST'):
               id_tag = Checks.IntorNone(request.POST.get("id_tag"), None)
               if id_tag is not None:
                    try:
                         t_b = tag_base.objects.get(id=request.POST.get('id_tag'))
                         try:
                              tag_interest.objects.get(tag = t_b, user = request.user).delete()
                              return HttpResponse(f'- {t_b.id} {t_b.title}')
                         except:
                              tag_interest_new = tag_interest(user=request.user, tag=t_b)
                              tag_interest_new.save()
                              return HttpResponse(f'+ {t_b.id} {t_b.title}')
                    except:
                         return render(request, 'Errors/404.html')
               else:
                    return render(request, 'Errors/404.html')
          else:
               tags = tag_base.objects.all()
               return render(request, TEMP_DIR + 'tag_list.html',
                             {"tags": tags})
     else:
          return render(request, 'Errors/404.html')