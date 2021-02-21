from .models import UserProfile

def category(request):
    return {"UserProfile": UserProfile.objects.get(id = request.user.id)}