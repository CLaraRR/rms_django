# Generated by Django 2.2.3 on 2019-07-06 16:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sno', models.CharField(blank=True, max_length=200)),
                ('sex', models.IntegerField()),
                ('birthday', models.DateField()),
                ('type', models.IntegerField()),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('create_time', models.DateField(blank=True, null=True)),
                ('total_hours', models.PositiveIntegerField()),
                ('credit', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['institute'],
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('found_time', models.DateField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('found_time', models.DateField(blank=True, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_num', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.Institute')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.Major')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.Semester')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.Year')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_grade1', models.PositiveIntegerField(default=0)),
                ('regular_grade2', models.PositiveIntegerField(default=0)),
                ('final_grade', models.PositiveIntegerField(default=0)),
                ('total_grade', models.PositiveIntegerField(default=0)),
                ('credit', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['course_id', 'student_id'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rms.Institute'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='section_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rms.SectionInfo'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
