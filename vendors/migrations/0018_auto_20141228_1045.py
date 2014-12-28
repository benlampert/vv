# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0017_auto_20141228_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation_name', models.CharField(max_length=200)),
                ('question', models.ManyToManyField(to='vendors.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='question',
            field=models.ForeignKey(to='vendors.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 28, 15, 45, 52, 886622, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
