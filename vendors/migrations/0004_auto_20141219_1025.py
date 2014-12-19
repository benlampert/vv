# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_auto_20141219_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vv_contract',
            field=models.BooleanField(default=0, verbose_name=b'is_vv'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 15, 25, 55, 61690, tzinfo=utc), verbose_name=b'date_added'),
            preserve_default=True,
        ),
    ]
