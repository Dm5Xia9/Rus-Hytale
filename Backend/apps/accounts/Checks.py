def nouname(User):
     return User.is_authenticated
from .models import User
def UpdatingParameters(request):
     if ValidityUsername(request.POST.get("username")):
          request.user.username = request.POST.get("username")
     else:
          return "ErrorUsername"

     if ValidityIdentifier(request.POST.get("identifier")):
          request.user.identifier = request.POST.get("identifier")
     else:
          return "ErrorIdentifier"
     try:
          request.user.DateBirth = request.POST.get("DateBirth")
     except:
          return "ErrorDateBirth"
     if request.user.avatar != request.FILES.get("ava") and request.FILES.get("ava") != None:
          request.user.avatar = request.FILES.get("ava")
     else:
          return "ErrorAvatar"
     request.user.first_name = request.POST.get("first_name")
     request.user.last_name = request.POST.get("last_name")
     request.user.city = request.POST.get("city")
     request.user.telephone = request.POST.get("telephone")
     return request
def ValidityUsername(input):
     if input.isalnum() and not User.objects.filter(username=input).exists():
          return True
     else:
          return False
def ValidityIdentifier(input):
     if input.isalnum() and not User.objects.filter(identifier=input).exists():
          return True
     else:
          return False
def ErrorsCheck(request):
     if isinstance(request, str):
          return False #Обработка ошибок
     else:
          return True
def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None
def messages_users_get(messages_count):
    if (len(User.objects.order_by('-messages_count')) < messages_count):
        Users_messages_count = User.objects.order_by('-messages_count')[:len(User.objects.order_by('-messages_count'))]
    else:
        Users_messages_count = User.objects.order_by('-messages_count')[:messages_count]
    return Users_messages_count
def points_users_get(Points):
    if (len(User.objects.order_by('-Points')) < Points):
        Users_Points = User.objects.order_by('-Points')[:len(User.objects.order_by('-Points'))]
    else:
        Users_Points = User.objects.order_by('-Points')[:Points]
    return Users_Points
def IntorNone(object, default):
    try:
        return int(object)
    except ValueError:
        return default