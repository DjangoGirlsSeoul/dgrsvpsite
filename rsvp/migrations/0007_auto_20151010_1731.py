# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0006_event_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime',
            new_name='start_time',
        ),
    ]
