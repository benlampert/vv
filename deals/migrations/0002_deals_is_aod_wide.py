# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='is_aod_wide',
            field=models.BooleanField(default=0, verbose_name=b'AOD-wide Deal'),
            preserve_default=True,
        ),
    ]
