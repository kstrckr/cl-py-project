# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 23:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0002_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 26, 23, 46, 38, 551068, tzinfo=utc)),
        ),
    ]