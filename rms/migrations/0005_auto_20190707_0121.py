# Generated by Django 2.2.3 on 2019-07-06 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0004_auto_20190707_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='section_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rms.SectionInfo'),
        ),
    ]
