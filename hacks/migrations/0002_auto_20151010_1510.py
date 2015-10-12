# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hack',
            name='cover_photo',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
