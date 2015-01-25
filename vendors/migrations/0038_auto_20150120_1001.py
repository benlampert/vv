# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0037_auto_20150120_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 15, 1, 28, 339574, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
