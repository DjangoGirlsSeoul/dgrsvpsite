# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(to='resources.Category', blank=True),
        ),
    ]
