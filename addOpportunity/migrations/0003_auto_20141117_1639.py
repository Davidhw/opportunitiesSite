# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addOpportunity', '0002_posting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='posting',
            name='hiringCriteria',
            field=models.TextField(max_length=500),
        ),
    ]
