# @Time    : 18-6-19 下午7:54
# @Author  : cuishu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from .views import BlogView,DetailView,blogdetail,like
urlpatterns = [
    url(r'^blog/$',BlogView.as_view(),name='blog'),
    url(r'^blogtwo/(?P<tid>\d+)/$',BlogView.as_view(),name='blogtwo'),
    url(r'^single-blog/(?P<pid>\d+)/$', DetailView.as_view(), name='detail'),
    url(r'^single-blog2/$', blogdetail, name='blogdetail'),
    url(r'^like/(\d+)$',like,name='like'),



]
