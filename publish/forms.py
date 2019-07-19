from django import forms
from django.forms import widgets
from .models import Report, Resource, Comment, Notice, Task, TaskScore
from rms.models import Course, Score


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'description', 'content']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control',}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'content': widgets.Textarea(attrs={'class': 'form-control'}),

        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description', 'category', 'version', 'author', 'file', 'image']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control',}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control m-bot15'}),
            'version': widgets.TextInput(attrs={'class': 'form-control'}),
            'author': widgets.TextInput(attrs={'class': 'form-control', }),
            'file': widgets.FileInput(),
            'image': widgets.FileInput(),


        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']
        widgets = {
            'content': widgets.TextInput(attrs={'class': 'form-control'}),
            'author': widgets.TextInput(attrs={'class': 'form-control'}),

        }


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['name', 'content', 'file', 'author']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'content': widgets.Textarea(attrs={'class': 'form-control'}),
            'file': widgets.FileInput(),
            'author': widgets.TextInput(attrs={'class': 'form-control'}),
        }



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'create_time', 'total_hours', 'credit', 'teacher', 'institute']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'create_time': widgets.DateInput(attrs={'class': 'form-control'}),
            'total_hours': widgets.NumberInput(attrs={'class': 'form-control'}),
            'credit': widgets.NumberInput(attrs={'class': 'form-control'}),
            'teacher': widgets.Select(attrs={'class': 'form-control m-bot15'}),
            'institute': widgets.Select(attrs={'class': 'form-control m-bot15'}),


        }



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'content', 'appendix', ]
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),

            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'content': widgets.Textarea(attrs={'class': 'form-control'}),
            # 'deadline_time': widgets.DateTimeInput(attrs={'class': 'form-control'}),
            'appendix': widgets.FileInput(),

        }


class TaskSubmitForm(forms.ModelForm):
    class Meta:
        model = TaskScore
        fields = ['file']
        widgets = {
            'file': widgets.FileInput(),
        }






