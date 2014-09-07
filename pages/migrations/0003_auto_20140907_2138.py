# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20140907_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('parent__position', 'position')},
        ),
    ]
