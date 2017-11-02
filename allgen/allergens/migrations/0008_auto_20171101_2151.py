# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 01:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0007_auto_20171101_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 1, 51, 21, 471983, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
    ]
