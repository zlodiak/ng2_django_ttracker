# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0003_auto_20171210_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(to='app_tasks.Status'),
        ),
    ]
