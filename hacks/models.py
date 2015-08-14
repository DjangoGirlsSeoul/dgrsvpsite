from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify


class Hack(models.Model):
    title  = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400)
    long_description =  models.TextField()
    github_link = models.URLField(max_length=250, blank=True)
    ppt_link = models.URLField(max_length=250, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    cover_photo =  models.ImageField(upload_to='uploads',blank=True)
    category  = models.ManyToManyField(Category, blank=True, null=True, through='CategoryToHack')
    writer = models.ForeignKey(User)
    updatedAt =  models.DateTimeField(auto_now=True)
	createdAt =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self):
		if not self.id:
			self.createdAt = timezone.now()
			self.post_slug = slugify(self.title)
		self.updatedAt = timezone.now()
		return super(Hack,self).save()


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug


class CategoryToHack(models.Model):
    hack = models.ForeignKey(Hack)
    category = models.ForeignKey(Category)
