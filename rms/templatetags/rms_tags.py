from django import template
from django.db.models.aggregates import Count
from publish.models import Category, Resource, Notice, TaskScore
from django.db.models import Q


register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_most_read_resources(num = 5):
    return Resource.objects.all().order_by('-views')[:num]


@register.simple_tag
def get_latest_notices(num = 5):
    return Notice.objects.all().order_by('-create_time')[:num]


@register.inclusion_tag('undo_tasks.html')
def get_undo_tasks(student_id):
    task_score_list = TaskScore.objects.filter(Q(student_id = student_id)&Q(is_complete = False))

    return {'task_score_list': task_score_list}


@register.filter
def chinese(x):
    if x == 'male':
        return '男'
    elif x == 'female':
        return '女'
    elif x == 'unknown':
        return '未知'
    elif x == 'student':
        return '学生'
    elif x == 'teacher':
        return '教师'
    elif x == 'admin':
        return '管理员'
    elif x == 'autumn':
        return '秋季学期'
    elif x == 'spring':
        return '春季学期'
    elif x == 'summer':
        return '夏季学期'



@register.filter
def floatbeautiful(x):
    return '{:g}'.format(x)