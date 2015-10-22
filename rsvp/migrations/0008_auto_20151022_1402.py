# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_auto_20151010_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
