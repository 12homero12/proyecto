# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20141007_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
