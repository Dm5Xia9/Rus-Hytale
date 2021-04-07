from django.shortcuts import render,redirect
from .models import communiti, tag, tag, communiti_interest
from articles.models import tag_base
import re
from .forms import communiti_createForm
from articles import Checks
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
TEMP_DIR = "communities/"
# Create your views here.
@csrf_exempt
def communities(request):
     from .models import communiti
     communities = communiti.objects.all()
     if request.user.is_authenticated:
          if (request.method == 'POST'):
               id_communiti = request.POST.get("id_tag")
               if id_communiti is not None:
                    try:
                         request.user.communiti_interest_set.get(communiti=communiti.objects.get(identifier=id_communiti)).delete()
                         comm_this = communiti.objects.get(identifier=id_communiti)
                         comm_this.subscribers = len(comm_this.communiti_interest_set.all())
                         comm_this.save()
                         return HttpResponse(f'- {id_communiti} {communiti.objects.get(identifier=id_communiti).title} {comm_this.subscribers}')
                    except:
                         comm_interes = communiti_interest(user = request.user, communiti=communiti.objects.get(identifier=id_communiti))
                         comm_interes.save()
                         comm_this = communiti.objects.get(identifier=id_communiti)
                         comm_this.subscribers = len(comm_this.communiti_interest_set.all())
                         comm_this.save()
                         return HttpResponse(f'+ {id_communiti} {communiti.objects.get(identifier=id_communiti).title} {comm_this.subscribers}')
          communiti_ones = request.user.communiti_set.all()
          if len(communiti_ones) == 1:
               return render(request, TEMP_DIR + 'communities.html', {'communities': communities, 'communiti_c': True, 'my_communiti': communiti_ones[0]})
          elif len(communiti_ones) == 0:
               return render(request, TEMP_DIR + 'communities.html', {'communities': communities, 'communiti_c': False})
          else:
               for i in communiti_ones:
                    if i.id != communiti_ones[0].id:
                         i.delete()

               return render(request, TEMP_DIR + 'communities.html', {'communities': communities, 'communiti_c': True, 'my_communiti': communiti_ones[0]})
     return render(request, TEMP_DIR + 'communities.html', {'communities':communities})
def communiti_create(request):
     from .models import communiti, tag
     if request.user.is_authenticated and len(request.user.communiti_set.all()) == 0:
          if request.method == "POST":
               form = communiti_createForm(request.POST)
               if form.is_valid():
                    new_communiti = form.save()
                    if request.FILES.get("ava") != None:
                         new_communiti.ava = request.FILES.get("ava")
                    new_communiti.owner = request.user
                    new_communiti.save()
                    new_communiti.identifier = 'id'+str(new_communiti.id)
                    new_communiti.save()
                    tags = request.POST.get("tags").split(' ')
                    if tags == []:
                         print('нуль')
                    else:
                         tags = [i for i in tags if i]
                         tags = [i.lower() for i in re.sub(r'[^\w\s]+|[\d]+', '', " ".join(tags)).strip().split(' ') if
                                 i.lower()]
                         for i in tags:
                              tag_new = tag(communiti=new_communiti, title = i)
                              tag_new.save()
                              try:
                                   tag_base.objects.get(title = i)
                              except:
                                   tag_base_new = tag_base(title = i)
                                   tag_base_new.save()
                    return redirect('/communities/')
               else:
                    return render(request, TEMP_DIR + 'communiti_create.html', {'form': form})
          else:
               form = communiti_createForm()
               return render(request, TEMP_DIR + 'communiti_create.html', {'form': form})
     else:
          return render(request, 'Errors/404.html')
def communiti(request, communiti_identifier):
     from .models import communiti, tag
     communiti_c = communiti.objects.get(identifier = communiti_identifier)
     return render(request, TEMP_DIR + 'communiti.html', {'communiti': communiti_c})
