from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = "resource_categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/resource_categories/%s/" % self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Category,self).save(*args, **kwargs)

class Resource(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    description = models.TextField(default='')
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Resource,self).save(*args, **kwargs)
