from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^(?P<slug>[-_\w]+)/$', views.resourceDetail, name = 'resourceDetail'),
    url(r'^add/$', views.add_resource, name='add_resource'),
    url(r'^$', views.index, name='index'),
]
