# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20160421_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(blank=True, to='resources.Category', null=True),
        ),
    ]
