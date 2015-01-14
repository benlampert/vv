# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0026_auto_20150105_1605'),
        ('evaluations', '0003_question_for_marketing'),
    ]

    operations = [
        migrations.CreateModel(
            name='MT_VendorAnswers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.FloatField(default=0.0)),
                ('question', models.ForeignKey(related_name='question', to='evaluations.Question')),
                ('vendor', models.ForeignKey(related_name='vendor', to='vendors.Vendor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='questions', to='evaluations.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='vendor_evaluation',
            field=models.ForeignKey(related_name='vendor_eval', to='evaluations.VendorEvaluation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evaluations',
            name='eval_name',
            field=models.CharField(default=b'New Evaluation', max_length=100),
            preserve_default=True,
        ),
    ]
