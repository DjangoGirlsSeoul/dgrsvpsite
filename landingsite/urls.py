from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact-us/email/$', views.contact, name='contact'),
    url(r'^contact-us/thanks/',TemplateView.as_view(template_name='landingsite/thanks.html'),name='thanks'),
    url(r'^contact-us/',TemplateView.as_view(template_name='landingsite/contact_us.html'),name='contact-us'),
    url(r'^about-us/',TemplateView.as_view(template_name='landingsite/about_us.html'),name='about-us'),
]
