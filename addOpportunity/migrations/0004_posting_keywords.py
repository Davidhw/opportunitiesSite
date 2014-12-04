# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addOpportunity', '0003_auto_20141117_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='keyWords',
            field=models.CharField(default='added before keywords was created, key2', max_length=100),
            preserve_default=False,
        ),
    ]
