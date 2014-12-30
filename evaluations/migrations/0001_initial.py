# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0022_auto_20141230_1730'),
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
            name='Evaluations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eval_name', models.CharField(default=b'new evaluation', max_length=100)),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
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
                ('section_evaluation', models.ManyToManyField(related_name='sections', to='evaluations.Evaluations')),
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
                ('evaluation', models.ForeignKey(related_name='vendors_evaluation', to='evaluations.Evaluations')),
                ('vendor', models.ForeignKey(related_name='evaluation', to='vendors.Vendor')),
            ],
            options={
                'ordering': ['vendor'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='eval_section',
            field=models.ForeignKey(related_name='questions', to='evaluations.Section'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('eval_section', 'question_order')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='answers', to='evaluations.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='vendor_evaluation',
            field=models.ForeignKey(related_name='answers', to='evaluations.VendorEvaluation'),
            preserve_default=True,
        ),
    ]
