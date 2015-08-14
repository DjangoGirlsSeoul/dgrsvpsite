# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryToHack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('category', models.ForeignKey(to='hacks.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Hack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=400)),
                ('long_description', models.TextField()),
                ('github_link', models.URLField(max_length=250, blank=True)),
                ('ppt_link', models.URLField(max_length=250, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('cover_photo', models.ImageField(upload_to='uploads', blank=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(null=True, to='hacks.Category', through='hacks.CategoryToHack', blank=True)),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='categorytohack',
            name='hack',
            field=models.ForeignKey(to='hacks.Hack'),
        ),
    ]
