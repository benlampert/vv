# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0034_auto_20150118_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 18, 20, 27, 11, 742463, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
