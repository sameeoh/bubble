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
    url(r'^add_order$', views.add_order),
    #remove during production
    url(r'^dev$', views.dev),
    url(r'^dev/text$', views.text),
    url(r'^payment$', views.payment),
    url(r'^checkout$', views.checkout),
    #redirect to admin page
    url(r'^admin/$', views.admin),
    url(r'^admin/orderinfo/(?P<id>\d+)$', views.orderinfo),
    # url(r'^orderinfo/(?P<id>\d+$', views.orderinfo)

]
