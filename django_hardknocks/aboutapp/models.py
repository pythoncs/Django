from django.db import models

# Create your models here.

#联系我们
class Contact(models.Model):
    c_name = models.CharField(max_length=30,verbose_name='客户姓名')
    c_email = models.EmailField(verbose_name='客户邮箱',blank=False)
    c_message = models.TextField(verbose_name='客户留言',blank=True)
    c_date = models.DateTimeField(auto_now=True,verbose_name='留言时间')

    class Meta():
        verbose_name = '联系我们'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.c_name

#公司信息
class Us(models.Model):
    c_content = models.TextField(verbose_name='contact us content')
    u_tel = models.CharField(max_length=11,verbose_name='电话')
    u_fax = models.CharField(max_length=20,verbose_name='传真')
    u_email = models.EmailField(verbose_name='邮箱')
    u_address = models.CharField(max_length=100,verbose_name='地址')

    class Meta():
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name
#产品页
class WorkPage(models.Model):
    wp_title = models.CharField(max_length=30,verbose_name='产品页标题')
    wp_cintent = models.TextField(verbose_name='产品介绍')

    class Meta():
        verbose_name = '产品页'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.wp_title

#产品分类
class WorkCategory(models.Model):
    wc_name = models.CharField(max_length=30,verbose_name='产品分类名称')

    class Meta():
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.wc_name

#产品
class Work(models.Model):
    w_title = models.CharField(max_length=30,verbose_name='产品标题')
    w_image = models.ImageField(upload_to='static/img',verbose_name='产品')
    w_describe = models.TextField(verbose_name='产品描述')
    w_date = models.DateTimeField(auto_now=True,verbose_name='产品上传时间')
    w_category = models.ManyToManyField(WorkCategory,verbose_name='产品分类')

    class Meta():
        verbose_name = '产品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.w_title

#产品分类2
class WorkCategoryTwo(models.Model):
    wc_name = models.CharField(max_length=30,verbose_name='产品分类名称')

    class Meta():
        verbose_name = '产品分类二'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.wc_name


#产品大图
class WorkTwo(models.Model):
    w_class = models.CharField(max_length=30,verbose_name='类')
    w_title = models.CharField(max_length=30,verbose_name='产品标题')
    w_image = models.ImageField(upload_to='static/img',verbose_name='产品')
    w_describe = models.TextField(verbose_name='产品描述')
    w_date = models.DateTimeField(auto_now=True,verbose_name='产品上传时间')
    w_category = models.ManyToManyField(WorkCategoryTwo,verbose_name='产品分类')

    class Meta():
        verbose_name = '产品大'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.w_title
#关于HD
class AboutHd(models.Model):
    a_about = models.CharField(max_length=40,verbose_name='关于HD')
    a_title = models.CharField(max_length=100,verbose_name='标题')
    a_intro = models.TextField(verbose_name='HD简介')
    a_image = models.ImageField(upload_to='static/img')

    class Meta():
        verbose_name = '关于HD'
        verbose_name_plural = verbose_name


#背后的科学
class ScienceBehind(models.Model):
    s_bigtitle = models.CharField(max_length=50,verbose_name='大标题')
    s_title = models.CharField(max_length=50,verbose_name='标题')
    s_image = models.ImageField(upload_to='static/img',verbose_name='image')
    s_content = models.TextField(verbose_name='内容')

    class Meta():
        verbose_name = '背后的科学'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_title

#技术
class Skill(models.Model):
    s_title = models.CharField(max_length=40,verbose_name='技术名称')
    s_level = models.CharField(max_length=20,verbose_name='技術水平')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')

    class Meta():
        verbose_name = '技术'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_title

#焦点
class FocusPoints(models.Model):
    f_image = models.ImageField(upload_to='static/img')

    class Meta():
        verbose_name = '焦点'
        verbose_name_plural = verbose_name

#团队
class Team(models.Model):
    t_name = models.CharField(max_length=30,verbose_name='工作人员姓名')
    t_post = models.CharField(max_length=30,verbose_name='职位')
    t_intro = models.TextField(verbose_name='人员简介')
    t_picture = models.ImageField(upload_to='static/img',verbose_name='人员照片')
    t_gender = models.BooleanField(default=False,verbose_name='性别,默认为女')
    t_contribute = models.IntegerField(verbose_name='贡献值',default=0)

    class Meta():
        verbose_name = '团队'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.t_name

class SideShow(models.Model):
    s_cover = models.ImageField(upload_to='static/img/fullscreen',verbose_name='图片路径')
    s_title = models.CharField(max_length=30,verbose_name='轮播图标题')
    s_idx = models.IntegerField(verbose_name='索引')
    is_active = models.BooleanField(default=False,verbose_name='是否激活')

    class Meta():
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.s_title
