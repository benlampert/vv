# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20141218_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(default=(b'EMPTY', b'Update'), max_length=100, verbose_name=b'vendor_type', choices=[(b'DSP', b'Demand Side Platform'), (b'DMP', b'Data Management Platform'), (b'PMD', b'Preferred Marketing Developer'), (b'SSP', b'Supply Side Platform'), (b'PUB', b'Publisher'), (b'DATA', b'Data Source'), (b'ADS', b'Ad Server')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 15, 18, 40, 668028, tzinfo=utc), verbose_name=b'date_added'),
            preserve_default=True,
        ),
    ]
