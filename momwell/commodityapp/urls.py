from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^login/$',login,name='login'),
    url(r'^logout/$',logout,name='logout'),
    url(r'^about/$',about,name='about'),
    url(r'^commoditys/(?P<cid>\d*)/(?P<pindex>\d*)/(?P<sid>\d*)/$',commoditys,name='commoditys'),
    url(r'^details/(?P<cid>\d*)/(?P<bid>\d*)/$',details,name='details'),
    # url(r'^groupdetail/(\d*)/$',group_detail,name='groupdetail'),
    url(r'^buytoday/$',buyToday,name='buyToday'),
    url(r'^information/$',information,name='information'),
    url(r'^shopcart/(?P<cid>\d*)/$',ShopcartsView.as_view(),name='shopcart'),
    url(r'^shopcart_delete/(?P<cid>\d*)/$',delete,name='shopcart_delete'),
    url(r'^settlement/$',settlement,name='settlement'),
    url(r'^register/$',register,name='register'),
    url(r'^search/$',Search(),name='search'),




]