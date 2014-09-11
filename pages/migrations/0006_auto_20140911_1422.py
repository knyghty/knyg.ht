# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20140911_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(unique=True, max_length=255, blank=True),
        ),
    ]
