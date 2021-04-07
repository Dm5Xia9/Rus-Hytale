from django.shortcuts import render
from .models import  article_image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def file(request):
     if request.method == "POST":
          try:
               im = article_image(image=request.FILES.get('file'))
               im.save()
               return JsonResponse({'location': f'http://127.0.0.1:8000{im.image.url}'})
          except:
               return render(request, 'Errors/404.html')
     else:
          return render(request, 'Errors/404.html')