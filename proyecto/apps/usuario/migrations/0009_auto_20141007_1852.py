# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20141007_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='nombre_pre',
            new_name='pregunta',
        ),
    ]
