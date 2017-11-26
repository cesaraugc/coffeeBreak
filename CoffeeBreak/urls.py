from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^cadastro/$', views.post_new, name='post_new'),
    url(r'^login/$', views.loginView, name= 'loginView'),
    url(r'^logout/$', views.logoutView, name= 'logoutView'),
    url(r'^home/$', views.postLoginView, name= 'postLoginView'),
    url(r'^novoCB/$', views.CBNewView, name = 'CBNewView'),
    url(r'^map/$', views.mapaView, name = 'mapaView'),

]
