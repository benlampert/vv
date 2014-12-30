# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0020_auto_20141230_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 22, 22, 48, 17066, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
