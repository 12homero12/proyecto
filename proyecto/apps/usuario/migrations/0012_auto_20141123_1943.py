# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0011_auto_20141007_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='pre',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='res',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
        migrations.DeleteModel(
            name='Tema',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
