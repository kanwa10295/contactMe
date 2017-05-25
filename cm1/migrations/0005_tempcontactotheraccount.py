# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cm1', '0004_auto_20170328_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempContactOtherAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(max_length=50)),
                ('other_account', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('social_media_source', models.CharField(choices=[('', ''), ('_Propagated', '_Propagated'), ('Facebook', 'Facebook'), ('GooglePlus', 'GooglePlus'), ('LinkedIn', 'LinkedIn'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Pinterest', 'Pinterest'), ('Foursquare', 'Foursquare')], default='', max_length=50)),
                ('temp_id', models.CharField(max_length=12)),
                ('temp_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_contact_other_accounts', to='cm1.TempContact')),
            ],
            options={
                'verbose_name_plural': 'Temporary Contact Other Accounts',
            },
        ),
    ]
