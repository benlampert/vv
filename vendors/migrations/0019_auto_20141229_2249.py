# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0018_auto_20141229_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eval_question_name', models.CharField(max_length=300)),
                ('question_order', models.IntegerField()),
            ],
            options={
                'ordering': ['question_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.CharField(max_length=100)),
                ('section_order', models.IntegerField()),
                ('section_evaluation', models.ForeignKey(related_name='sections', to='vendors.Evaluations')),
            ],
            options={
                'ordering': ['section_order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VendorEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation', models.ForeignKey(related_name='vendors_evaluations', to='vendors.Evaluations')),
                ('vendor', models.ForeignKey(related_name='evaluations', to='vendors.Vendor')),
            ],
            options={
                'ordering': ['vendor'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set([('section_evaluation', 'section_order')]),
        ),
        migrations.AddField(
            model_name='question',
            name='eval_section',
            field=models.ForeignKey(related_name='questions', to='vendors.Section'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('eval_section', 'question_order')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='vendors.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='vendor_evaluation',
            field=models.ForeignKey(related_name='answers', to='vendors.VendorEvaluation'),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='evaluations',
            options={'verbose_name': 'Evaluation', 'verbose_name_plural': 'Evaluations'},
        ),
        migrations.AlterField(
            model_name='vendor',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 30, 3, 49, 19, 950036, tzinfo=utc), verbose_name=b'Date Added'),
            preserve_default=True,
        ),
    ]
