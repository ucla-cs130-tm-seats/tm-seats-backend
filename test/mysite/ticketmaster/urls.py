from django.conf.urls import patterns, url

from ticketmaster import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='index'),
  url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
  url(r'Login/$', views.login, name='login'),
  url(r'Validate/$', views.validate,  name='validate'),
)
