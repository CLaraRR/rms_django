# Generated by Django 2.2.3 on 2019-07-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0007_report_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publish.Resource', verbose_name='举报资源'),
        ),
    ]
