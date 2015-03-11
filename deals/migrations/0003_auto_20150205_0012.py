# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0052_auto_20150205_0012'),
        ('deals', '0002_sites'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='min_spend',
            field=models.CharField(default=b'none', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sites',
            name='preferred_conduit',
            field=models.ForeignKey(default=1, to='vendors.Inventory'),
            preserve_default=True,
        ),
    ]
