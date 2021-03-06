# Generated by Django 2.2.3 on 2019-07-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0015_notice_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='downloads',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='下载次数'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览次数'),
        ),
    ]
