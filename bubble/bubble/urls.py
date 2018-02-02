from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.main.urls')),
    url(r'^vendor/', include('apps.vendor.urls')),
]
