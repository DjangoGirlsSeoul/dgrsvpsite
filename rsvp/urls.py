from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-_\w]+)/$', views.event_detail, name='event_detail'),
    url(r'^$', views.events_list, name='events_list'),
    url(r'^event_signup/(?P<event_id>[0-9]+)/$', views.event_signup, name='event_signup'),
    url(r'^myevents$', views.user_rsvplist, name='user_rsvplist'),
]
