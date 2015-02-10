# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0010_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Cred_Roles',
        ),
    ]
