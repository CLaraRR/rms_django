from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'description', 'create_time', 'modify_time', 'deadline_time', 'author', 'complete_num', 'views')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'modify_time', 'author', 'views')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_time', 'author', 'is_view', 'is_manage')

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'version', 'create_time', 'author', 'views')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('resource', 'content', 'author', 'create_time')



admin.site.register(Task, TaskAdmin)
admin.site.register(TaskScore)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Category)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Comment, CommentAdmin)