# Generated by Django 2.2.3 on 2019-07-06 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import publish.models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0002_auto_20190707_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='资源类别'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='name',
            field=models.CharField(max_length=200, verbose_name='通知标题'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览数'),
        ),
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='举报人'),
        ),
        migrations.AlterField(
            model_name='report',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='report',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_manage',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否被处理'),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_view',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否被查看'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=200, verbose_name='举报标题'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(max_length=200, verbose_name='资源名称'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='version',
            field=models.CharField(max_length=100, verbose_name='版本号'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览数'),
        ),
        migrations.AlterField(
            model_name='task',
            name='appendix',
            field=models.FileField(blank=True, null=True, upload_to=publish.models.task_directory_path, verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='task',
            name='complete_num',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='完成人数'),
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='提交截止日期'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_allow_upload',
            field=models.BooleanField(default=False, verbose_name='是否允许上传附件'),
        ),
        migrations.AlterField(
            model_name='task',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, verbose_name='任务标题'),
        ),
        migrations.AlterField(
            model_name='task',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='浏览数'),
        ),
        migrations.AlterField(
            model_name='taskscore',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=publish.models.task_directory_path, verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='taskscore',
            name='is_complete',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否完成'),
        ),
        migrations.AlterField(
            model_name='taskscore',
            name='score',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='成绩'),
        ),
        migrations.AlterField(
            model_name='taskscore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='学生'),
        ),
        migrations.AlterField(
            model_name='taskscore',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publish.Task', verbose_name='任务标题'),
        ),
    ]
