from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 用户模型
class Hduser(AbstractUser):
    hname = models.CharField(max_length=20, verbose_name='姓名')
    # hpwd = models.CharField(max_length=16,verbose_name='密码')
    # hemail = models.EmailField(max_length=50,verbose_name='邮箱')
    # hdate = models.DateTimeField(auto_now=True,)
    # class Meta():

    verbose_name = '用户'
    verbose_name_plural = verbose_name


def __str__(self):
    return self.hname


# email验证
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50, default='', verbose_name='验证码')
    email = models.EmailField(max_length=50, blank=True, null=True)
    send_type = models.CharField(verbose_name='验证码类型',
                                 choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')),
                                 max_length=30)
    sed_time = models.DateTimeField(verbose_name='发送时间', auto_now=True)
    tel = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "邮箱验证码"
        # 复数
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
