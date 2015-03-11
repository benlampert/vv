# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0051_auto_20150205_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 5, 5, 12, 35, 794395, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
