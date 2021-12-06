# Generated by Django 3.2.9 on 2021-11-28 16:34

import asterisk.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushAck',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('SIPUsername', models.CharField(max_length=20, verbose_name='Sip Username')),
                ('Ack', models.BooleanField(default=False, verbose_name='Ack')),
                ('CallFrom', models.CharField(max_length=20, verbose_name='Call From')),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated On')),
            ],
            options={
                'verbose_name': 'Push Ack',
                'verbose_name_plural': 'Push Ack',
            },
        ),
        migrations.CreateModel(
            name='PushReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SIPUsername', models.CharField(max_length=20, unique=True, verbose_name='Sip Username')),
                ('PushKey', models.CharField(max_length=250, verbose_name='Push Key')),
                ('DeviceType', models.PositiveSmallIntegerField(choices=[(1, 'ANDROID'), (2, 'IOS')], default=asterisk.models.DeviceType['ANDROID'], verbose_name='Device Type')),
                ('CreatedOn', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated On')),
            ],
            options={
                'verbose_name': 'Push Registry',
                'verbose_name_plural': 'Push Registry',
            },
        ),
    ]
