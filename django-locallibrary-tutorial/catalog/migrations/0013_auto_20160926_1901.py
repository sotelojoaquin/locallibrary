# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_bookinstance_date_acquired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='date_acquired',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
