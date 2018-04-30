from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'(?P<depart_id>[0-9]+)/(?P<subject_id>[0-9]+)/(?P<practicle_id>[0-9]+)/$', views.view_codes, name='codes'),
    url(r'(?P<depart_id>[0-9]+)/(?P<subject_id>[0-9]+)/$', views.view_pre_codes, name='pre_codes'),
    url(r'', views.index, name='index'),
]
