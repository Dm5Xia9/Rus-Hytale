from accounts.models import User, tag_interest, user_interest
from communities.models import communiti_interest, communiti
from .models import article_top, tag_base
def top_article(request):
     return {"top_article": article_top.objects.all()[0]}
def tags_p(request):
     if(request.user.is_authenticated):
          return {"tags_p": request.user.tag_interest_set.all()}
     else:
          return {"tags_p": tag_base.objects.all()}
def comms_p(request):
     if(request.user.is_authenticated):
          print(request.user.communiti_interest_set.all())
          return {"comms_p": request.user.communiti_interest_set.all()}
     else:
          return {"comms_p": communiti.objects.all()}
def accs_p(request):
     if(request.user.is_authenticated):
          print(request.user.communiti_interest_set.all())
          return {"accs_p": request.user.user_interest_set.all()}
     else:
          return {"accs_p": User.objects.all()}