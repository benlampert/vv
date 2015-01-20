# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0004_auto_20150105_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mt_vendoranswers',
            options={'verbose_name': 'Vendor Answer', 'verbose_name_plural': 'Vendor Answers'},
        ),
    ]
