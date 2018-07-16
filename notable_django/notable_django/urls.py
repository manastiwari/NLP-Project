from django.contrib import admin
from django.conf.urls import *
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', (admin.site.urls)),
    url(r'^api/', include('api.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
