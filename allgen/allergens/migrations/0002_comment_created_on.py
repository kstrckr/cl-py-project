# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]