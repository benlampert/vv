# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0048_auto_20150205_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 5, 4, 12, 791568, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
