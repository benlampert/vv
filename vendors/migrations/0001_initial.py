# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_name', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField(default=datetime.datetime(2014, 12, 18, 16, 34, 1, 272384, tzinfo=utc), verbose_name=b'date_added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
