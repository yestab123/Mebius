# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0006_remove_saltminion_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saltminion',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已经认证'), (2, '未认证')], verbose_name='认证状态'),
        ),
    ]
