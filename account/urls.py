from django.conf.urls import patterns, url
from apps.account import views

urlpatterns = patterns('',
    url(r'^$', views.account_profile, name='profile'),
    url(r'^profile/$', views.account_profile, name='profile'),
    url(r'^login/$', views.account_login, name='login'),
    url(r'^logout/$', views.account_logout, name='logout'),
    url(r'^nda/$', views.account_nda, name='nda'),
    url(r'^recover/$', views.account_recover, name='recover'),
)