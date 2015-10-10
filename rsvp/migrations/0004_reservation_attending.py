# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_event_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='attending',
            field=models.BooleanField(default=False),
        ),
    ]
