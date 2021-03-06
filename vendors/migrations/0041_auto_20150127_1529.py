# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0040_auto_20150127_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 27, 20, 29, 42, 571522, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
