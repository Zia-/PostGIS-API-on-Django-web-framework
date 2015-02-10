# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0011_delete_user_cred_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Cred_Roles',
            fields=[
                ('id_user', models.AutoField(serialize=False, primary_key=True)),
                ('session_key', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=100)),
                ('pgr_astarfromatob', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
