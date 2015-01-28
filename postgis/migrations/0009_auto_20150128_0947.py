# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0008_user_cred_roles_pgr_astarfromatob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_cred_roles',
            name='session_key',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
