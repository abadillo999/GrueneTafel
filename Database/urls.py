from django.conf.urls import url
from Database import views


urlpatterns = [
    url(r'^layers/$', views.layer_list),
    url(r'^layers/(?P<pk>[0-9]+)/$', views.layer_detail),
    url(r'^home/$', views.mapas),
    url(r'^$', views.mapas)]

