# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20140907_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='test', max_length=64),
            preserve_default=False,
        ),
    ]
