from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import datetime


# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length = 200, verbose_name='学院名称')
    found_time = models.DateField(blank = True, null = True, verbose_name='成立时间')
    location = models.TextField(blank = True, null = True, verbose_name='所在地址')
    teacher_num = models.PositiveIntegerField(default=0, editable=False, verbose_name='教师人数')

    def increase_teacher_num(self):
        self.teacher_num += 1
        self.save(update_fields=['teacher_num'])

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length = 200, verbose_name='专业名称')
    found_time = models.DateField(blank = True, null = True, verbose_name='成立日期')
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE, verbose_name='所在学院')
    # student_num = models.PositiveIntegerField(default = 0, blank=True)

    def __str__(self):
        return self.name


class SectionInfo(models.Model):
    year = models.CharField(max_length=100, default=datetime.datetime.now().year, verbose_name='入学年份')
    semester = models.CharField(max_length=100, choices=(('autumn', u'秋季学期'), ('spring', u'春季学期'), ('summer',u'夏季学期')), default='autumn', verbose_name='学期')
    institute = models.ForeignKey(Institute, on_delete=models.DO_NOTHING, verbose_name='学院')
    major = models.ForeignKey(Major, on_delete = models.DO_NOTHING, verbose_name='专业')
    student_num = models.PositiveIntegerField(default=0, blank=True, null=True, editable=False, verbose_name='学生人数')

    def increase_student_num(self):
        self.student_num += 1
        self.save(update_fields=['student_num'])

    def __str__(self):
        return str(self.institute) + ' ' + str(self.major) + '专业 ' + str(self.year) + '级'

    class Meta:
        ordering = ['-year', 'semester', 'institute', 'major']



class User(AbstractUser):
    sno = models.CharField(max_length=200, blank=True, null=True, verbose_name='学工号')
    section_info = models.ForeignKey(SectionInfo, null=True, on_delete=models.DO_NOTHING, verbose_name='部门信息')
    # enroll_year = models.ForeignKey(EachYearMajorInfo, on_delete=models.CASCADE)
    # institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null = True)
    # major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True, blank=True)
    # class_num = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=8, choices=(("male", u"男"), ("female", u"女"),("unknown", u"未知")), default="male",verbose_name="性别")
    birthday = models.DateField(null=True, verbose_name='出生日期')
    type = models.CharField(max_length=8, choices=(('student', u'学生'), ('teacher', u'教师'), ('unknown', u'未知')), default="student",verbose_name='类型')
    # level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.sno:
            sno_str = ''
            if self.section_info:
                if self.type == 'student':
                    self.section_info.increase_student_num()
                    sno_str = str(self.section_info.year) + str('%04d' % self.section_info.institute_id) + str('%04d' % self.section_info.major_id) + str('%04d' % self.section_info.student_num)
                else:
                    self.section_info.institute.increase_teacher_num()
                    sno_str = str(self.section_info.year) + str('%04d' % self.section_info.institute_id) + str('%04d' % self.section_info.institute.teacher_num)
            self.sno = sno_str
        super(User, self).save(*args, **kwargs)


    class Meta(AbstractUser.Meta):
        pass





class Course(models.Model):
    name = models.CharField(max_length = 200, verbose_name='课程名称')
    create_time = models.DateField(blank = True,null=True, verbose_name='成立时间')
    total_hours = models.PositiveIntegerField(verbose_name='总学时')
    credit = models.PositiveIntegerField(verbose_name='学分')
    teacher = models.ForeignKey(User, limit_choices_to={'type': 'teacher'}, null = True, blank=True, on_delete = models.SET_NULL, verbose_name='任教老师')
    institute = models.ForeignKey(Institute, null = True, blank=True, on_delete = models.SET_NULL, verbose_name='开办学院')
    regular_proportion1 = models.FloatField(default=0.1, verbose_name='平时成绩1占百分比')
    regular_proportion2 = models.FloatField(default=0.4, verbose_name='平时成绩2占百分比')
    final_proportion = models.FloatField(default=0.5, verbose_name='期末成绩占百分比')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['institute']


class Score(models.Model):
    course = models.ForeignKey(Course, on_delete = models.DO_NOTHING, verbose_name='课程名称')
    student = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='学生')
    regular_grade1 = models.FloatField(default = 0.0, verbose_name='平时成绩1')
    regular_grade2 = models.FloatField(default = 0.0, verbose_name='平时成绩2')
    final_grade = models.FloatField(default = 0.0, verbose_name='期末成绩')
    total_grade = models.FloatField(default = 0.0, verbose_name='总成绩')
    credit = models.PositiveIntegerField(default = 0, verbose_name='获得学分绩点')

    class Meta:
        ordering = ['course_id', 'student_id']

