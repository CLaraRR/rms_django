# Generated by Django 2.2.3 on 2019-07-13 12:07

from django.db import migrations, models
import publish.models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0014_auto_20190712_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=publish.models.notice_directory_path, verbose_name='文件'),
        ),
    ]
