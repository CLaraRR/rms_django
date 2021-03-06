# Generated by Django 2.2.3 on 2019-07-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0009_auto_20190711_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='downloads',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='下载次数'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览数'),
        ),
    ]
