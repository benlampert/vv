# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='section_evaluation',
        ),
        migrations.AddField(
            model_name='evaluations',
            name='added_sections',
            field=models.ManyToManyField(to='evaluations.Section'),
            preserve_default=True,
        ),
    ]
