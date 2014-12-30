# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0023_auto_20141230_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='vendor_evaluation',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='question',
            name='eval_section',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='section',
            name='section_evaluation',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.RemoveField(
            model_name='vendorevaluation',
            name='evaluation',
        ),
        migrations.DeleteModel(
            name='Evaluations',
        ),
        migrations.RemoveField(
            model_name='vendorevaluation',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='VendorEvaluation',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 23, 5, 45, 312585, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
