from django.shortcuts import render, reverse
from django.views.generic.base import View
from aboutapp.models import SideShow
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hduser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

def base(request):
    user_list = Hduser.objects.all()
    for users in user_list:
        user = users
    ctx = {
        'user':user,
    }
    return render(request,'base.html',ctx)
class LoginView(View):
    def get(self, request):
        side_list = SideShow.objects.all()
        user_list = Hduser.objects.all()
        ctx = {
            'side_list': side_list,
            'user_list':user_list,
        }
        return render(request, 'login.html', ctx)

    def post(self, request):
        side_list = SideShow.objects.all()
        itusername = request.POST.get('username')
        itpassword = request.POST.get('password')
        user = authenticate(username=itusername, password=itpassword)
        users = Hduser.objects.get(username=itusername)

        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = users.id
                return HttpResponseRedirect(reverse("hardknocks:index"))
            else:
                return render(request, 'login.html', {'error_msg': '用户未激活！'})
        else:
            return render(request, 'login.html', {'error_msg': '用户名或者密码错误！'})
        # if user.username == itusername:
        #     ituser = Hduser.objects.get(hname=itusername)
        #     if itpassword == ituser.password:
        #         return HttpResponseRedirect(reverse('hardknocks:index'))
        #     else:
        #         return render(request,'login.html',{'error_msg':'用户或密码错误','side_list':side_list})
        # else:
        #     return render(request, 'login.html', {'error_msg': '用户或密码错误','side_list':side_list})


class RegisterView(View):

    def get(self, request):
        side_list = SideShow.objects.all()
        ctx = {
            'side_list': side_list
        }
        return render(request, 'register.html', ctx)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        hdwuse = Hduser()
        hdwuse.hname = username
        hdwuse.password = make_password(password)
        hdwuse.username = username
        hdwuse.is_active = True
        hdwuse.save()
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("hardknocks:index"))