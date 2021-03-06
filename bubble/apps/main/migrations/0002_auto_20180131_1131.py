# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='main.Order'),
        ),
        migrations.AlterField(
            model_name='listitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='main.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='special',
            field=models.TextField(default='None'),
        ),
    ]
