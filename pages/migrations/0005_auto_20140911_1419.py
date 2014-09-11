# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
