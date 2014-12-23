# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0013_auto_20141221_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name': 'Platform', 'verbose_name_plural': 'Platforms'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 18, 37, 37, 517648, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
