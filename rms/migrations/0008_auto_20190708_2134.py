# Generated by Django 2.2.3 on 2019-07-08 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0007_auto_20190708_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioninfo',
            name='year',
            field=models.CharField(default=datetime.datetime.now, max_length=100, verbose_name='入学年份'),
        ),
    ]
