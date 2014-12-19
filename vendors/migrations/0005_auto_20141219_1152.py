# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20141219_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_blurb',
            field=models.CharField(default=b'empty', max_length=400, verbose_name=b'vendor_blurb'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 16, 52, 17, 42417, tzinfo=utc), verbose_name=b'date_added'),
            preserve_default=True,
        ),
    ]
