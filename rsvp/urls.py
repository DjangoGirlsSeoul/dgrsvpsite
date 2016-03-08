from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^myevents$', views.user_rsvplist, name='user_rsvplist'),
    url(r'^(?P<slug>[-_\w]+)/$', views.event_detail, name='event_detail'),
    url(r'^events$', views.events_list, name='events_list'),
    url(r'^event_signup/(?P<event_id>[0-9]+)/$', views.event_signup, name='event_signup'),
]
