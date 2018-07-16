from django.contrib import admin
from django.conf.urls import *
from Database import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]