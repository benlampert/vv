# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_auto_20150120_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='price_q2',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deals',
            name='price_q3',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deals',
            name='price_q4',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
