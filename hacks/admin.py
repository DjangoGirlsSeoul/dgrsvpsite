from django.contrib import admin
from .models import Hack, Category
from django.template.defaultfilters import slugify

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class HackAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Hack,HackAdmin)
admin.site.register(Category, CategoryAdmin)
