# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='roles',
            field=models.IntegerField(default=0),
        ),
    ]
