from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from api.views import hello
from api.views import hel
from api.views import upload_file

admin.autodiscover()

urlpatterns = [
    url(r'^hello/', hello , name = 'hello'),
    url(r'^hello2/', upload_file, name='hel')

]
