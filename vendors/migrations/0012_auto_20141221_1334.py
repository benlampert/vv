# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0011_auto_20141221_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data_source',
            options={'verbose_name': 'Data Source', 'verbose_name_plural': 'Data Sources'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 18, 34, 41, 531885, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
