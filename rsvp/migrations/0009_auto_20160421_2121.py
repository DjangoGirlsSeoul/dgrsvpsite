# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_auto_20151022_1402'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['-createdAt']},
        ),
    ]
