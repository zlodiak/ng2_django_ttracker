# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from app_tasks.models import Status


class Migration(migrations.Migration):

    dependencies = [
        ('app_tasks', '0002_task_deadline_date'),
    ]

    operations = [
      migrations.AlterField('Task', 'status', models.ForeignKey(Status, default=1))
    ]
