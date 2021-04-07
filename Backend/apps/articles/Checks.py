from .models import article, Like, Delike, article_image, views_article, tag_base
from accounts.models import User
def checking_id(answer_id):
     if answer_id is not None:
          try:
               return article.objects.get(id=IntorNone(answer_id, None))
          except:
               return None
     else:
          return None
def checking_tag_id(answer_tag_id):
     if answer_tag_id is not None:
          try:
               return tag_base.objects.get(id=IntorNone(answer_tag_id, None))
          except:
               return None
     else:
          return None
def checking_user_id(answer_user_id):
     if answer_user_id is not None:
          try:
               return User.objects.get(id=IntorNone(answer_user_id, None))
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
def likeBoolCheck(request, answer_id):
     try:
          request.user.like_set.get(user=request.user, article=answer_id)
          return False
     except ObjectDoesNotExist:
          return True
def dilikeBoolCheck(request, answer_id):
     try:
          request.user.delike_set.get(user=request.user, article=answer_id)
          return False
     except ObjectDoesNotExist:
          return True

