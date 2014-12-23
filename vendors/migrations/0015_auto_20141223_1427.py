# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0014_auto_20141221_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adserver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adserver_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Ad Server',
                'verbose_name_plural': 'Ad Servers',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vendor',
            name='integrated_adservers',
            field=models.ManyToManyField(to='vendors.Adserver'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 19, 27, 44, 982196, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
