from django.contrib import admin
from .models import Resource,Category

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class ResourceAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Resource,ResourceAdmin)
admin.site.register(Category,CategoryAdmin)
