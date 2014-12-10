from django.conf.urls import url

from ticketmaster import views

urlpatterns = [
    url(r'^[A-Z0-9]{16}/geometry/$', views.geometry),
    url(r'^[A-Z0-9]{16}/summary/$', views.summary),
    url(r'^get/price/$', views.getSegPrice),
    url(r'^filter/price/$', views.filterByPrice),
    url(r'^reserve/$', views.reserve),
    url(r'^login/$', views.validate),
    url(r'^get/place/$', views.getSegPlace),
]

