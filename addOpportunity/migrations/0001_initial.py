# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('positionType', models.CharField(default=b'J', max_length=1, choices=[(b'J', b'Job'), (b'I', b'Internship'), (b'V', b'Volunteering Opportunity')])),
                ('title', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=500)),
                ('hiringCriteria', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
