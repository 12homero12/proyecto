# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temas', '0003_sala'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'permissions': ('registrar_tema', 'registrar_tema')},
        ),
    ]
