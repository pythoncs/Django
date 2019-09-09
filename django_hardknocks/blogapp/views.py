from django.shortcuts import render,reverse,render_to_response
from django.views.generic.base import View
from .models import BlogPage,Post,Tags,Comment,PostUser,Postlike
from  aboutapp.models import SideShow
from userapp.models import Hduser
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
class BlogView(View):
    def get(self,request,tid=-1):
        side_list = SideShow.objects.all()
        #博客页内容
        blogpage = BlogPage.objects.all()
        #博客内容
        if tid != -1:
            tag = Tags.objects.get(id=tid)
            post_list = tag.post_set.all()
        else:
            post_list = Post.objects.all()

        ctx = {
            'side_list': side_list,
            'blpgpage':blogpage,
            'post_list':post_list,
        }
        return render(request, 'blog.html', ctx)

    def post(self,request):
        pass

class DetailView(View):
    def get(self,request,pid):
        side_list = SideShow.objects.all()
        #获取到的博客
        posts = Post.objects.get(id=pid)
        tags_list = posts.p_tags.all()
        #博客页内容
        blogpage = BlogPage.objects.all()
        # 博客浏览量--------------------------------------------------------------------------
        #获取当前用户
        user_id = request.session['user_id']
        pu = PostUser()
        pu.p_id = posts.id
        pu.u_id = user_id
        pu.save()
        postid_list = PostUser.objects.filter(p_id=posts.id)
        userid_list = []
        for user in postid_list:
            userid_list.append(user.u_id)
            userid_list = list(set(userid_list))
        posts.p_views = len(userid_list)
        posts.save()
        ctx = {
            'side_list': side_list,
            'posts':posts,
            'blogpage':blogpage,
            'tags_list':tags_list,

        }
        return render(request, 'single-blog.html', ctx)

    def post(self, request,pid):
        # 评论
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        cwebsite = request.POST.get('cwebsite')
        comment = request.POST.get('comment')
        post = Post.objects.get(id=pid)

        vcmt = Comment()
        vcmt.c_post = post
        vcmt.c_name2 = cname
        vcmt.c_email = cemail
        vcmt.c_website = cwebsite
        vcmt.c_content = comment
        vcmt.save()
        return HttpResponseRedirect(reverse('hardknocks:index'))

def blogdetail(request):
    side_list = SideShow.objects.all()
    # 博客页内容
    blogpage = BlogPage.objects.all()
    posts = Post.objects.get(id=1)
    user_list = Hduser.objects.all()
    for users in user_list:
        user = users
    ctx = {
        'side_list':side_list,
        'posts':posts,
        'blogpage':blogpage,
        'user':user
    }
    return render(request,'single-blog.html',ctx)

def like(request,pid):
    post = Post.objects.get(id=pid)
    # post.p_likes = post.p_likes + 1
    # post.save()
    user_id = request.session['user_id']
    pl = Postlike()
    pl.u_id = user_id
    pl.p_id = post.id
    pl.save()
    postid_list = PostUser.objects.filter(p_id=post.id)
    userid_list = []
    for user in postid_list:
        userid_list.append(user.u_id)
        userid_list = list(set(userid_list))
    post.p_likes = len(userid_list) + 100
    post.save()

    return JsonResponse({'plike':post.p_likes})

