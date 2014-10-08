# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20141007_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='nombre_tema',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
