# Generated by Django 2.2.3 on 2019-07-08 15:01

from django.db import migrations, models
import publish.models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0004_auto_20190708_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='file',
            field=models.FileField(default=1, upload_to=publish.models.resource_directory_path, verbose_name='上传资源'),
            preserve_default=False,
        ),
    ]
