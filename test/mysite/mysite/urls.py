from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ticketmaster/login', 'ticketmaster.views.login'),
    url(r'^ticketmaster/', include('ticketmaster.urls', namespace="ticketmaster")),
    url(r'^admin/', include(admin.site.urls)),
)
