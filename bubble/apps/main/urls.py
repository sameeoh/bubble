from django.conf.urls import url
from . import views


urlpatterns = [
    #login and registration render
    url(r'^$', views.index),
    #login/logout/register process
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    #home page w/ past orders
    url(r'^dashboard$', views.dashboard),
    #add order html render
    url(r'^order$', views.order),
    #add_order process
    url(r'^order/(?P<id>\d+)$', views.add_order),
    #remove during production
    url(r'^dev$', views.dev),
    url(r'^dev/text$', views.text),

]