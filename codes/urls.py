from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'sub/(?P<subject_id>[0-9]+)/$', views.detail_subject, name='detail_subject'),
    url(r'pract/(?P<practicle_id>[0-9]+)/$', views.detail_practicle, name='detail_practicle'),
    url(r'', views.index, name='homepage'),
]
