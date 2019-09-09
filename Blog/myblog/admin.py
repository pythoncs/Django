from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #默认显示在页面顶部
    actions_on_top = True
    #显示字段
    list_display = ['atitle','apub_datetime']
    #对指定字段的值进行过滤
    list_filter = ['atitle']
    #分页
    list_per_page = 5
    #搜索框
    search_fields = ['atitle']
   #  #分组显示
   #  fieldsets = [
   #      ('base',{'fields':['atitle']}),
   #      ('other',{'fields':['acontent']})
   # ]
admin.site.register(Article,ArticleAdmin)