# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position_app', '0003_point'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='fonction',
            new_name='function',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='fonction',
            new_name='function',
        ),
        migrations.AlterField(
            model_name='member',
            name='m_type',
            field=models.CharField(choices=[('LOADER', 'Loader'), ('WAREHOUSEMAN', 'Warehouseman'), ('TRANSPORTER', 'Transporter')], max_length=200),
        ),
    ]