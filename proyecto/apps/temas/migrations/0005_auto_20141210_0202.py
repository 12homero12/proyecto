# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0004_auto_20141210_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'permissions': (('registrar_tema', 'registrar_tema'),)},
        ),
    ]
