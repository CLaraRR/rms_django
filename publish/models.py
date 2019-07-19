from django.db import models
from rms.models import User, Course


# Create your models here.
def task_directory_path(instance, filename):
    return 'tasks/{0}/{1}'.format(instance.pk, filename)

def task_submit_directory_path(instance, filename):
    return 'tasks_submit/{0}/{1}'.format(instance.task.pk, filename)


def resource_directory_path(instance, filename):
    return 'resources/{0}/{1}'.format(instance.category.pk, filename)


def image_directory_path(instance, imagename):
    return 'images/{0}'.format(imagename)


def notice_directory_path(instance, filename):
    return 'notices/{0}'.format(filename)



class Task(models.Model):
    name = models.CharField(max_length = 200, verbose_name='任务标题')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程名称')
    description = models.TextField(verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    is_allow_upload = models.BooleanField(default = False, verbose_name='是否允许上传附件')
    create_time = models.DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now = True, verbose_name='修改时间')
    deadline_time = models.DateTimeField(verbose_name='提交截止日期')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    # students = models.ManyToManyField(Student)
    appendix = models.FileField(upload_to = task_directory_path, null=True,blank=True, verbose_name='附件')
    complete_num = models.PositiveIntegerField(default = 0, editable = False, verbose_name='完成人数')
    views = models.PositiveIntegerField(default = 0, editable = False, verbose_name='浏览数')


    def __str__(self):
        return self.name

    def increase_views(self):
        self.views += 1
        self.save(update_fields = ['views'])

    def increase_complete_num(self):
        self.complete_num += 1
        self.save(update_fields = ['complete_num'])


    class Meta:
        ordering = ['-create_time']


class TaskScore(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE, verbose_name='任务标题')
    student = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='学生')
    file = models.FileField(upload_to = task_submit_directory_path, null=True, blank=True, verbose_name='文件')
    is_complete = models.BooleanField(default = False, blank = True, verbose_name='是否完成')
    score = models.PositiveIntegerField(default = 0, blank = True, verbose_name='成绩')


class Notice(models.Model):
    name = models.CharField(max_length = 200, verbose_name='通知标题')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now = True, verbose_name='修改时间')
    file = models.FileField(upload_to = notice_directory_path, null=True, blank=True, verbose_name='文件')
    author = models.CharField(max_length=100, verbose_name='创建者')
    views = models.PositiveIntegerField(default = 0, editable = False, verbose_name='浏览次数')
    downloads = models.PositiveIntegerField(default=0, editable=False, verbose_name='下载次数')


    def __str__(self):
        return self.name

    def increase_views(self):
        self.views += 1
        self.save(update_fields = ['views'])

    def increase_downloads(self):
        self.downloads += 1
        self.save(update_fields=['downloads'])

    class Meta:
        ordering = ['-create_time']


class Report(models.Model):
    name = models.CharField(max_length = 200, verbose_name='举报标题')
    resource = models.ForeignKey('Resource', on_delete=models.DO_NOTHING, verbose_name='举报资源')
    description = models.TextField(verbose_name='描述')
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add = True, verbose_name='创建时间')
    author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, verbose_name='举报人')
    is_view = models.BooleanField(default = False, blank=True, verbose_name='是否被查看')
    is_manage = models.BooleanField(default = False, blank=True, verbose_name='是否被处理')

    def __str__(self):
        return self.name

    def view_status(self):
        self.is_view = True
        self.save(update_fields=['is_view'])

    def manage_status(self):
        self.is_manage = True
        self.save(update_fields=['is_manage'])


    class Meta:
        ordering = ['-create_time']


class Category(models.Model):
    name = models.CharField(max_length = 200, verbose_name='资源类别')

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length = 200, verbose_name='资源名称')
    description = models.TextField(verbose_name='描述')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name='类别')
    version = models.CharField(max_length = 100, blank=True, null=True, verbose_name='版本号')
    author = models.CharField(max_length=100, default='匿名', null = True, verbose_name='创建者')
    file = models.FileField(upload_to=resource_directory_path, verbose_name='上传资源')
    image = models.ImageField(upload_to=image_directory_path, verbose_name='资源图标')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    views = models.PositiveIntegerField(default = 0, editable = False, verbose_name='浏览数')
    downloads = models.PositiveIntegerField(default=0, editable=False, verbose_name='下载次数')


    def __str__(self):
        return self.name

    def increase_views(self):
        self.views += 1
        self.save(update_fields = ['views'])

    def increase_downloads(self):
        self.downloads += 1
        self.save(update_fields = ['downloads'])

    class Meta:
        ordering = ['-views']



class Comment(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-create_time']