# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0032_auto_20150118_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 17, 53, 34, 409368, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
