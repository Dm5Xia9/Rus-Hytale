from .models import User, user_post
def category(request):
     if(request.user.is_authenticated):
          if request.user.identifier == None:
               request.user.identifier = 'id' + str(request.user.id)
               request.user.save()
               return {"User": request.user}
          else:
               return {"User": request.user}
     else:
          return {"User": request.user}
