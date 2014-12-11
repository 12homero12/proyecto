# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_crearsala_mensaje'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CrearSala',
            new_name='Sala',
        ),
    ]
