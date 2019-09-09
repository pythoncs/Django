from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^detail/(\d*)$', views.detail, name='detail'),
    url(r'^editpage/$', views.editpage, name='editpage'),
    url(r'^editpagehandle/$', views.editpage_handle, name='editpagehandle'),
    url(r'^change/(\d+)$', views.change, name='change'),
    url(r'^changehandle/(\d+)$', views.changehandle, name='changehandle'),
    url(r'^del/(\d+)$', views.Del,name='del'),
    url(r'^signin$', views.signIn, name='sign'),
    url(r'^signinhandle$', views.signInHandle, name='signinhandle'),
    url(r'^rigister$', views.Register, name='register'),
    url(r'^rigisterhandle$', views.Register_handle, name='registerhandle'),

]
