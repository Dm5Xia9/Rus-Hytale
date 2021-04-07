from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import User, user_post
from .forms import CustomUserLoginForm, CustomUserCreateForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from . import Checks
from django.contrib import messages
TEMP_DIR = "accounts/"

def register(request):
    if not Checks.nouname(request.user):  # Пользователь не авторизован
        if request.method == "POST":  # Происходит после POST
            form = CustomUserCreateForm(request.POST)
            if form.is_valid(): #Форма валидна
                new_user = form.save()
                new_user.identifier = 'id' + str(new_user.id)
                new_user.save()
                login(request, new_user)
                return redirect('/accounts/' + new_user.identifier + '/')
            else: #Форма не валидна
                return render(request,'registration/reg.html', {'form': form})
        else:  # Происходит без POST
           form = CustomUserCreateForm()
           return render(request,'registration/reg.html', {'form': form})
    else:# Пользователь авторизован
         return render(request, 'Errors/404.html')
def auth(request):
    if not Checks.nouname(request.user):
        if request.method == "POST":
            form = CustomUserLoginForm(request.POST)
            if form.is_valid():
                user = form.save()
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        us = User.objects.get(username = user.username)
                        return redirect('/accounts/' + us.identifier + '/')
                    else:
                        messages.error(request, 'Ваша учетная запись отключена')
                        return render(request, 'registration/login.html', {'form': form})
                else:
                    messages.error(request, 'Неверный логин или пароль')
                    return render(request, 'registration/login.html', {'form': form})
            else:
                return render(request, 'registration/login.html', {'form': form})
        else:
            form = CustomUserLoginForm
            return render(request, 'registration/login.html', {'form': form})
    else:
        return render(request, 'Errors/404.html')
from django.views.decorators.csrf import csrf_exempt
step_posts = 6
@csrf_exempt
def prof(request, identifier):
    UserNow = Checks.get_or_none(User, identifier = identifier)
    if UserNow is not None: #Аккаунь существует
        if Checks.nouname(request.user):#Я зарагистрирован
            if request.user.id == UserNow.id: #Это мой профиль
                if request.method == 'POST':
                    try:
                        if request.POST.get('type') == '0':
                            UserNow = Checks.get_or_none(User, identifier=identifier)
                            if request.user.id == UserNow.id:
                                user_post_new = user_post(user_post=request.user, content=request.POST.get('content'))
                                user_post_new.save()
                                return JsonResponse({'text_post': user_post_new.content})
                        else:
                            lastPost = int(request.POST.get('last_post'))
                            new_Posts = UserNow.user_post_set.all()[::-1]
                            new_Posts = new_Posts[lastPost:lastPost+step_posts]
                            data_posts_user_ava_url = []
                            data_posts_user_username = []
                            data_posts_content = []
                            data_posts_id = []
                            for post in new_Posts:
                                data_posts_id.append(post.id)
                                data_posts_user_ava_url.append(post.user_post.avatar.url)
                                data_posts_user_username.append(post.user_post.username)
                                data_posts_content.append(post.content)
                            return JsonResponse({'ids':data_posts_id, 'avatars': data_posts_user_ava_url, 'usernames': data_posts_user_username, 'contents': data_posts_content, 'len':lastPost+10})
                    except:
                        StartPosts = UserNow.user_post_set.all()[::-1]
                        StartPosts = StartPosts[:step_posts]
                        return render(request, TEMP_DIR + 'prof/account.html',
                                      {'UserNow': UserNow, 'StartPosts': StartPosts})
                else:
                    StartPosts = UserNow.user_post_set.all()[::-1]
                    StartPosts = StartPosts[:step_posts]
                    return render(request, TEMP_DIR + 'prof/account.html', {'UserNow': UserNow, 'StartPosts':StartPosts})
            else: #Я не зарагистрирован
                StartPosts = UserNow.user_post_set.all()[::-1]
                StartPosts = StartPosts[:step_posts]
                return render(request, TEMP_DIR + 'prof/account.html', {'UserNow': UserNow, 'StartPosts': StartPosts})
        else: #Это не мой профиль
            StartPosts = UserNow.user_post_set.all()[::-1]
            StartPosts = StartPosts[:step_posts]
            return render(request, TEMP_DIR + 'prof/account.html', {'UserNow': UserNow, 'StartPosts': StartPosts})
    else:#Аккаун не существует
        return render(request, 'Errors/404.html')

def settings(request):
    if Checks.nouname(request.user): #Пользователь авторизован
        if request.method == "POST": #Происходит после POST
            request = Checks.UpdatingParameters(request)
            if Checks.ErrorsCheck(request):#ошибок нет
                request.user.save()
                return redirect('/accounts/' + request.user.identifier + '/')
        else: #Происходит без POST
            return render(request, TEMP_DIR + 'settings/Settings.html')
    else: #Пользователь не авторизован
        return render(request, 'Errors/404.html')