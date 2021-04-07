from accounts.models import User
from .models import New
from communities.models import communiti
def checking_id(answer_id):
     if answer_id is not None:
          try:
               return New.objects.get(id=IntorNone(answer_id, None))
          except:
               return None
     else:
          return None
def checking_communiti_id(answer_communiti_id):
     if answer_communiti_id is not None:
          try:
               return communiti.objects.get(id=IntorNone(answer_communiti_id, None))
          except:
               return None
     else:
          return None
def IntorNone(object, default):
    try:
        return int(object)
    except ValueError:
        return default
from django.core.exceptions import ObjectDoesNotExist
def likeBoolCheck(request, new_id):
     try:
          request.user.like_new_set.get(user=request.user, new=new_id)
          return False
     except ObjectDoesNotExist:
          return True
def dilikeBoolCheck(request, new_id):
     try:
          request.user.delike_new_set.get(user=request.user, new=new_id)
          return False
     except ObjectDoesNotExist:
          return True

