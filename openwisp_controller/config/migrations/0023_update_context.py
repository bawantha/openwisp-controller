# Generated by Django 3.0.3 on 2020-02-26 19:58

import collections
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0022_vpn_format_dh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='context',
            field=jsonfield.fields.JSONField(blank=True, default=dict, dump_kwargs={'ensure_ascii': False, 'indent': 4}, help_text='Additional <a href="http://netjsonconfig.openwisp.org/en/stable/general/basics.html#context" target="_blank">context (configuration variables)</a> in JSON format', load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
    ]
