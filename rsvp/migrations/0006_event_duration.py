# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0005_auto_20151010_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
