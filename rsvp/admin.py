from django.contrib import admin
from .models import Event, Reservation

from django_markdown.admin import AdminMarkdownWidget

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    formfield_overrides = {'notes': {'widget': AdminMarkdownWidget}}
admin.site.register(Event, EventAdmin)
admin.site.register(Reservation)
