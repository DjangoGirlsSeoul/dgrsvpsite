from django.contrib import admin
from .models import Event, Reservation

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
admin.site.register(Event, EventAdmin)
admin.site.register(Reservation)
