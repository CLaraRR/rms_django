# Generated by Django 2.2.3 on 2019-07-15 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0017_auto_20190714_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='final_proportion',
            field=models.FloatField(default=0.5, verbose_name='期末成绩占百分比'),
        ),
        migrations.AddField(
            model_name='course',
            name='regular_proportion1',
            field=models.FloatField(default=0.1, verbose_name='平时成绩1占百分比'),
        ),
        migrations.AddField(
            model_name='course',
            name='regular_proportion2',
            field=models.FloatField(default=0.4, verbose_name='平时成绩2占百分比'),
        ),
    ]
