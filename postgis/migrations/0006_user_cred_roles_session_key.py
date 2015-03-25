# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0005_remove_user_cred_roles_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_cred_roles',
            name='session_key',
            field=models.CharField(default=b'null', max_length=100),
            preserve_default=True,
        ),
    ]
