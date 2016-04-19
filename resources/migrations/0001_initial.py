# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name_plural': 'resource_categories',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('description', models.TextField(default='')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(to='resources.Category')),
            ],
        ),
    ]
