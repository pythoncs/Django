# @Time    : 18-6-17 下午12:45
# @Author  : cuishu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from .views import IndexView,AboutView,OurWorkView,oneColumn,ContactView
urlpatterns = [
    url(r'^index/$',IndexView.as_view(),name='index'),
    url(r'^about/$',AboutView.as_view(),name='about'),
    url(r'^ourwork/$',OurWorkView.as_view(),name='ourwork'),
    url(r'^onecolumn/$',oneColumn, name='onecolumn'),
    url(r'^contact/$',ContactView.as_view(),name='contact'),
    # url(r'^workdetail/(?P<wid>\d+)/$',workDetail,name='workdetail')

]
