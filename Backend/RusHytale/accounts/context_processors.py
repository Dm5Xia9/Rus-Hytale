from .models import UserProfile

def category(request):
    if request.user.is_authenticated:
        try:
            UP = UserProfile.objects.get(id=request.user.id)
            return {"UserProfile": UP}
        except:
            UP = UserProfile()
            UP.user_id = request.user.id
            UP.identifier = 'id' + str(request.user.id)
            UP.save()
            return {"UserProfile": UserProfile.objects.get(id=request.user.id)}
    else:
        return ''