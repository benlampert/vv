# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0016_auto_20141229_2206'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Evaluation',
            new_name='Evaluations',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 3, 6, 30, 609264, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
