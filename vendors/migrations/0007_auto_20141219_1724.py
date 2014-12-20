# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0006_auto_20141219_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vv_nda',
            field=models.BooleanField(default=0, verbose_name=b'Vivaki NDA signed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 19, 22, 24, 21, 84956, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_blurb',
            field=models.TextField(default=b'empty', max_length=400, verbose_name=b'Short Blurb'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_external_pov',
            field=models.TextField(default=b'empty', max_length=1000, verbose_name=b'External POV'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_internal_pov',
            field=models.TextField(default=b'empty', max_length=1000, verbose_name=b'Internal POV'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_type',
            field=models.CharField(default=(b'EMPTY', b'Update'), max_length=100, verbose_name=b'Category', choices=[(b'DSP', b'Demand Side Platform'), (b'DMP', b'Data Management Platform'), (b'PMD', b'Preferred Marketing Developer'), (b'SSP', b'Supply Side Platform'), (b'PUB', b'Publisher'), (b'DATA', b'Data Source'), (b'ADS', b'Ad Server')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vv_contract',
            field=models.BooleanField(default=0, verbose_name=b'Is Vivaki Verified'),
            preserve_default=True,
        ),
    ]
