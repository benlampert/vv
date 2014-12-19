# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_auto_20141219_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_external_pov',
            field=models.CharField(default=b'empty', max_length=1000, verbose_name=b'vendor_external_pov'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_internal_pov',
            field=models.CharField(default=b'empty', max_length=1000, verbose_name=b'vendor_internal_pov'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 17, 1, 2, 495086, tzinfo=utc), verbose_name=b'date_added'),
            preserve_default=True,
        ),
    ]
