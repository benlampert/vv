# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_deals_is_aod_wide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deals',
            name='price_q1',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
            preserve_default=True,
        ),
    ]
