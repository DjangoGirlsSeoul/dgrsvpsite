from django.contrib import admin
from .models import Hack, Category
from django.template.defaultfilters import slugify

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('title'),)}

class HackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('title'),)}

admin.site.register(Hack,HackAdmin)
admin.site.register(Category, CategoryAdmin)
