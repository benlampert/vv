# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_auto_20141220_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='integrated_vendor',
        ),
        migrations.AddField(
            model_name='vendor',
            name='integrated_inventory_sources',
            field=models.ManyToManyField(to='vendors.Inventory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 17, 12, 12, 167999, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
