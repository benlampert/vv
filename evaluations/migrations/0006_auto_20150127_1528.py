# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0005_auto_20150118_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mt_vendoranswers',
            options={'verbose_name': 'Vendor Eval Answer', 'verbose_name_plural': 'Vendor Eval Answers'},
        ),
    ]
