# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0009_auto_20141220_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_source_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vendor',
            name='integrated_data_sources',
            field=models.ManyToManyField(to='vendors.Data_Source'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 18, 27, 35, 940647, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
