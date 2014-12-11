# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0005_auto_20141210_0202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'permissions': ('bloques_permisos', 'bloques_permisos')},
        ),
    ]
