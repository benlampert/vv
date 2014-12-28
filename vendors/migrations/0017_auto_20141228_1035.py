# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0016_auto_20141228_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='question',
            field=models.ManyToManyField(to='vendors.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 15, 35, 58, 693352, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
