from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', views.postSlug, name = 'postSlug'),
    url(r'^$', views.index, name='index'),
]
