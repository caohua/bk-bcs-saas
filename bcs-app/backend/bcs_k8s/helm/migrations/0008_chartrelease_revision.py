# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-03-19 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helm', '0007_chartrelease_valuefile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartrelease',
            name='revision',
            field=models.IntegerField(default=0, help_text='用来标识helm release的升级版本'),
        ),
    ]
