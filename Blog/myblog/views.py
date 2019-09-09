from django.shortcuts import render,redirect
from .models import *
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    list = Article.objects.filter(aisDelete=False)
    uname = request.session.get('uname')
    content = {'list':list,'uname':uname}

    return render(request,'myblog/index.html',content)

def detail(request,id):
    list = Article.objects.get(pk=id)
    content = {'list': list}
    return render(request,'myblog/detail.html',content)

def editpage(request):
    return render(request,'myblog/editpage.html')

def editpage_handle(request):
    title = request.POST.get('title','')
    content = request.POST.get('content','')

    a = Article()
    a.atitle = title
    a.acontent = content
    a.aread = 0
    a.save()
    # return render(request,'myblog/editpage_handle.html')
    return redirect(reverse('blog:index'))
def Del(request,id):
    a = Article.objects.get(pk=id)
    a.delete()
    return redirect(reverse('blog:index'))

def change(request,id):
    list2 = Article.objects.get(pk=id)
    content2 = {'list':list2}
    return render(request,'myblog/change.html',content2)

def changehandle(request,id):
    newtitle = request.POST['title']
    newcontent = request.POST['content']

    a2 = Article.objects.get(pk=id)
    a2.atitle = newtitle
    a2.acontent = newcontent
    a2.save()
    return render(request,'myblog/change_handle.html')

def signIn(request):
    return render(request,'myblog/sign_in.html')

def signInHandle(request):
    # uname = request.POST['uname']
    # upwd = request.POST['upwd']
    # ucontent = {'uname':uname,'upwd':upwd}
    # return render(request,'myblog/index.html',ucontent)
    # return render(request,'myblog/sign_in_handle.html',ucontent)
    request.session['uname'] = request.POST['uname']
    return redirect(reverse('blog:index'))

def Register(request):
    return render(request,'myblog/register.html')

def Register_handle(request):
    # uname = request.POST['uname']
    # upwd = request.POST['pwd']
    # rcontent = {'uname':uname,'upwd':upwd}
    # return render(request,'myblog/sign_in.html',rcontent)
    return redirect(reverse('blog:sign'))