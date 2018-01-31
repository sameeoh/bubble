from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.main.urls')),
    url(r'^vendor/', include('apps.vendor.urls')),
]
