
from django import template
from accounts.models import tag_interest, User
from communities.models import communiti_interest, communiti
from ..models import tag_base
register = template.Library()
def check(value, arg):
     tag_id = int(value)
     tag_b = tag_base.objects.get(id = tag_id)
     user_id = int(arg)
     user = User.objects.get(id = user_id)
     try:
          tag_b.tag_interest_set.get(user = user)
          return 'Отписаться'
     except:
          return 'Подписаться'
def check_comm(value, arg):
     comm_id = int(value)
     user_id = int(arg)
     user = User.objects.get(id = user_id)
     try:
          user.communiti_interest_set.get(communiti=communiti.objects.get(id=comm_id))
          return 'Отписаться'
     except:
          return 'Подписаться'
def check_acc(value, arg):
     comm_id = int(value)
     user_id = int(arg)
     user = User.objects.get(id = user_id)
     try:
          user.user_interest_set.get(user_inter=User.objects.get(id=comm_id))
          return 'Отписаться'
     except:
          return 'Подписаться'
def cou(value):
     return len(value)
register.filter('check', check)
register.filter('cou', cou)
register.filter('check_acc', check_acc)
register.filter('check_comm', check_comm)