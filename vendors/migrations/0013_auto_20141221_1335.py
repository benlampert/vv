# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0012_auto_20141221_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory Source', 'verbose_name_plural': 'Inventory Sources'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 18, 35, 46, 447457, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
