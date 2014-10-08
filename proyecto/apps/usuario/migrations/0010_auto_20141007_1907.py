# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_auto_20141007_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='respuesta',
            field=models.CharField(max_length=500),
        ),
    ]
