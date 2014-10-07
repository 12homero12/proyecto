# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import proyecto.apps.usuario.thumbs
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0003_auto_20141006_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', proyecto.apps.usuario.thumbs.ImageWithThumbsField(upload_to=b'img_user')),
                ('usuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Email',
            field=models.EmailField(max_length=75, verbose_name=django.contrib.auth.models.User),
        ),
    ]
