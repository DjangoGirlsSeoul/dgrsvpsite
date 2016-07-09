"""code4every1site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^rsvp/', include('rsvp.urls', namespace="rsvp")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^ms-volunteer-registration/$',TemplateView.as_view(template_name="landingsite/volunteer_registration.html")),
    url(r'^ms-open-camp-registration/$',TemplateView.as_view(template_name="landingsite/ms-open-camp-registration.html")),
    url(r'^resources/', include('resources.urls', namespace="resources")),
    url(r'^cms/', include('cms.urls')),
    url(r'^', include('landingsite.urls', namespace="landingsite")),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
