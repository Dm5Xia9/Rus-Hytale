from . import Checks
from django.shortcuts import render
from .models import User, user_interest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
TEMP_DIR = "accounts/"
@csrf_exempt
def accs(request):
    if request.user.is_authenticated:
        if (request.method == 'POST'):
            identifier_user = request.POST.get("identifier_user")
            if identifier_user is not None:
                try:
                    request.user.user_interest_set.get(
                        user_inter=User.objects.get(identifier=identifier_user)).delete()
                    comm_this = User.objects.get(identifier=identifier_user)
                    comm_this.subscribers = len(comm_this.user_i.all())
                    comm_this.save()
                    return HttpResponse(
                        f'- {identifier_user} {User.objects.get(identifier=identifier_user).username} {comm_this.subscribers}')
                except:
                    comm_interes = user_interest(user=request.user,
                                                      user_inter=User.objects.get(identifier=identifier_user))
                    comm_interes.save()
                    comm_this = User.objects.get(identifier=identifier_user)
                    comm_this.subscribers = len(comm_this.user_i.all())
                    comm_this.save()
                    return HttpResponse(
                        f'+ {identifier_user} {User.objects.get(identifier=identifier_user).username} {comm_this.subscribers}')
    return render(request, TEMP_DIR + 'accs/accounts.html', {'accs': User.objects.all()})