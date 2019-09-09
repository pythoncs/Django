from django.db import models
from userapp.models import Hduser
# 博客页
class BlogPage(models.Model):
    b_intro = models.TextField(verbose_name='博客页简介')

    class Meta():
        verbose_name = '博客页'
        verbose_name_plural = verbose_name


#标签
class Tags(models.Model):
    t_name = models.CharField(max_length=30, verbose_name='标签')

    class Meta():
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.t_name


#博客分类
class Pcategory(models.Model):
    c_name = models.CharField(max_length=30,verbose_name='博客分类')
    is_delete = models.BooleanField(default=False)

    class Meta():
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name


#博客
class Post(models.Model):
    p_title = models.CharField(max_length=100,verbose_name='博客标题')
    p_content = models.TextField(verbose_name='博客内容')
    p_views = models.IntegerField(default=0,verbose_name='浏览量')
    p_date = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    p_author = models.CharField(max_length=30,verbose_name='作者')
    p_likes = models.IntegerField(default=100,verbose_name='点赞量')
    p_tags = models.ManyToManyField(Tags,verbose_name='标签')
    p_iamge = models.ImageField(upload_to='static/img',default=None)
    is_recommend = models.BooleanField(default=False,verbose_name='是否推荐')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    p_cate = models.ForeignKey(Pcategory,verbose_name='博客分类')

    class Meta():
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.p_title


# 评论
class Comment(models.Model):
    c_post = models.ForeignKey(Post,verbose_name='评论博客')
    # c_name = models.ForeignKey(Hduser, verbose_name='评论者')
    c_name2 = models.CharField(max_length=20,verbose_name='暂评论者')
    c_email = models.EmailField(blank=True,null=True, verbose_name='评论者邮箱')
    c_website = models.CharField(max_length=100, verbose_name='网页', blank=True,null=True)
    c_content = models.TextField(verbose_name='评论内容')
    c_date = models.DateTimeField(verbose_name='评论时间', auto_now=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name2


#浏览量
class PostUser(models.Model):
    p_id = models.IntegerField(max_length=40,verbose_name='博客id')
    u_id = models.IntegerField(max_length=40,verbose_name='用户id')

    class Meta():
        verbose_name = '浏览量'
        verbose_name_plural = verbose_name

#点赞
class Postlike(models.Model):
    p_id = models.IntegerField(max_length=40,verbose_name='博客id')
    u_id = models.IntegerField(max_length=40,verbose_name='用户id')

    class Meta():
        verbose_name = '点赞量'
        verbose_name_plural = verbose_name