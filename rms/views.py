from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse,  StreamingHttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from publish.models import *
from publish.forms import *
from django.db.models import Q
from .export_utils import *
from django import forms
import zipfile
from django.utils.encoding import escape_uri_path
from django.utils.http import urlquote




# Create your views here.
class IndexView(ListView):
    model = Resource
    template_name = 'rms/index.html'
    context_object_name = 'resources'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False

        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data



class ResourceView(DetailView):
    model = Resource
    template_name = 'rms/resource_page.html'
    context_object_name = 'resource'

    def get(self, request, *args, **kwargs):
        response = super(ResourceView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super(ResourceView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list,
        })
        return context


class CategoryView(ListView):
    model = Resource
    template_name = 'rms/resource_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category = cate)



class NoticeListView(ListView):
    model = Notice
    template_name = 'rms/notice_list.html'
    context_object_name = 'notices'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False

        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data


class NoticeDetialView(DetailView):
    model = Notice
    template_name = 'rms/notice_page.html'
    context_object_name = 'notice'

    def get(self, request, *args, **kwargs):
        response = super(NoticeDetialView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response


class ProfileView(DetailView):
    model = User
    template_name = 'rms/profile.html'
    context_object_name = 'user'


class ReportListView(ListView):
    model = Report
    template_name = 'rms/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.type != 'admin':
                author = get_object_or_404(User, pk=self.request.user.pk)
                return super(ReportListView, self).get_queryset().filter(author = author)
            else:
                return super(ReportListView, self).get_queryset().all()

        else:
            pass



class ReportDetialView(DetailView):
    model = Report
    template_name = 'rms/report_page.html'
    context_object_name = 'report'

    def get(self, request, *args, **kwargs):
        if self.request.user.type == 'admin':
            response = super(ReportDetialView, self).get(request, *args, **kwargs)
            self.object.view_status()
            return response
        else:
            response = super(ReportDetialView, self).get(request, *args, **kwargs)
            return response







class CourseListView(ListView):
    model = Course
    template_name = 'rms/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        if  self.request.user.is_authenticated:
            if self.request.user.type == 'admin':
                return super(CourseListView, self).get_queryset().all()

            elif self.request.user.type == 'teacher':
                teacher = get_object_or_404(User, pk = self.request.user.pk)
                return super(CourseListView, self).get_queryset().filter(teacher = teacher)

            elif self.request.user.type == 'student':
                student = get_object_or_404(User, pk = self.request.user.pk)
                score_list = Score.objects.filter(student = student)
                course_set = []
                for score in score_list:
                    course_set.append(get_object_or_404(Course, pk = score.course_id))
                return course_set
        else:
            pass



    # def get_context_data(self, **kwargs):
    #     if self.request.user.is_authenticated:
    #         # user_type = self.request.user.type
    #         if self.request.user.type == 'student':
    #             context = super().get_context_data(**kwargs)
    #             score_list = Score.objects.filter(student_id=self.request.user.pk)
    #             context.update({
    #                 'score_list':score_list,
    #             })
    #             return context
    #
    #     pass




class ScoreListView(ListView):
    model = Score
    template_name = 'rms/score_list.html'
    context_object_name = 'score_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.type == 'student':
                student = get_object_or_404(User, pk=self.request.user.pk)
                # score_list = Score.objects.filter(student=student)
                # return score_list
                return super(ScoreListView, self).get_queryset().filter(student=student)


            # elif self.request.user.type == 'teacher':
            #     course_id = self.request.GET.get('course_id')
            #     score_list = Score.objects.filter(course_id=course_id)
            #
            #     return score_list

        else:
            pass



class TaskListView(ListView):
    model = Task
    template_name = 'rms/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.type == 'teacher':
                author_id = self.request.user.pk
                # task_list = Task.objects.filter(author_id=author_id)
                # return task_list
                return super(TaskListView, self).get_queryset().filter(author_id=author_id)

            elif self.request.user.type == 'student':
                student_id = self.request.user.pk
                task_score_list = TaskScore.objects.filter(student_id=student_id)
                return task_score_list

            elif self.request.user.type == 'admin':
                return super(TaskListView, self).get_queryset().all()
        else:
            pass



class TaskDetailView(DetailView):
    model = Task
    template_name = 'rms/task_page.html'
    context_object_name = 'task'

    def get(self, request, *args, **kwargs):
        response = super(TaskDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        if self.request.user.type == 'student':
            task_id = self.object.pk
            student_id = self.request.user.pk
            task_score = get_object_or_404(TaskScore, Q(task_id = task_id)&Q(student_id = student_id))
            context.update({
                'taskscore': task_score,
            })
        return context



def download_resource(request, pk):
    resource_path = request.GET.get('file_path')
    resource_name = resource_path.split('/')[-1]
    file = open(resource_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(urlquote(resource_name))
    get_object_or_404(Resource, pk = pk).increase_downloads()
    return response



def resource_action(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('rms:index')

        # return redirect('/')
    else:
        form = ResourceForm()
    return render(request, 'rms/resource_form.html', {'form': form})



def report_action(request, pk):
    # redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = ReportForm(request.POST)

        if form.is_valid():
            report = form.save(commit = False)
            list = request.POST.getlist('checkbox_author')
            if len(list) == 0:
                report.author = get_object_or_404(User, pk = request.user.pk)

            report.resource = get_object_or_404(Resource, pk = pk)
            report.save()

            return redirect('rms:index')
    else:
        form = ReportForm()

    return render(request, 'rms/report_form.html', {'form': form, 'resource_id': pk})


def report_manage(request, pk):
    # redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        report = get_object_or_404(Report, pk=pk)
        report.manage_status()
        report.save()


    else:
        report = get_object_or_404(Report, pk = pk)

    return render(request, 'rms/report_page.html', {'report': report})


def report_delete(request, pk):

    Report(pk = pk).delete()


    return redirect('rms:report_list')



def notice_action(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            notice = form.save(commit = False)
            notice.save()

            return redirect('rms:notice_list')
    else:
        form = NoticeForm()

    return render(request, 'rms/notice_form.html', {'form': form})


def download_notice(request, pk):
    file_path = request.GET.get('file_path')
    file_name = file_path.split('/')[-1]
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(urlquote(file_name))
    get_object_or_404(Notice, pk = pk).increase_downloads()
    return response


def course_action(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course_obj = get_object_or_404(Course, pk = course_id)
            form = CourseForm(request.POST, instance = course_obj)
        else:
            form = CourseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('rms:course_list')
    else:
        course_id = request.GET.get('course_id')
        if course_id:
            c = get_object_or_404(Course, pk = course_id)
            form = CourseForm(instance = c)
            return render(request, 'rms/course_form.html', {'form': form, 'course_id': course_id})
        else:
            form = CourseForm()

    return render(request, 'rms/course_form.html', {'form': form})



def course_delete(request, pk):
    Course(pk = pk).delete()

    return redirect('rms:course_list')




def course_student(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        id_list = request.POST.getlist('student_list')
        id_list = [int(x) for x in id_list]
        # print(id_list)

        student_in_course = Score.objects.filter(course_id=course_id)
        student_in_course_id_list = []
        for student in student_in_course:
            student_in_course_id_list.append(student.student_id)
        # print(student_in_course_id_list)


        for id in id_list:
            if id not in student_in_course_id_list:
                Score.objects.create(course_id = course_id, student_id = id).save()


        for id in student_in_course_id_list:
            if id not in id_list:
                Score.objects.filter(Q(student_id=id)&Q(course_id=course_id)).delete()

        return redirect('rms:course_list')

    else:
        course_id = request.GET.get('course_id')
        sections = SectionInfo.objects.all()
        student_in_course = Score.objects.filter(course_id=course_id)
        student_in_course_id_list = []
        for student in student_in_course:
            student_in_course_id_list.append(student.student_id)


        return render(request, 'rms/course_student.html', {'sections': sections, 'course_id': course_id, 'students_in_course': student_in_course_id_list})




def course_equation(request, pk):

    if request.method == 'POST':
        course = get_object_or_404(Course, pk=pk)
        rg1 = float(request.POST['rg1'])
        rg2 = float(request.POST['rg2'])
        fg = float(request.POST['fg'])

        print(rg1 + rg2 + fg)
        if (rg1 + rg2 + fg) != 1.0:
            return HttpResponse('三类成绩占比加起来不等于1，请修改！！！')

        course.regular_proportion1 = rg1
        course.regular_proportion2 = rg2
        course.final_proportion = fg
        course.save()

        score_list = Score.objects.filter(course = course)
        for score in score_list:
            score.total_grade = score.regular_grade1 * course.regular_proportion1 + score.regular_grade2 * course.regular_proportion2 + score.final_grade * course.final_proportion
            score.save()

    else:
        course = get_object_or_404(Course, pk=pk)


    return render(request, 'rms/course_equation_form.html', {'course': course})






def score_action(request):
    if request.method == 'POST':
        id = request.POST.get('score_id')
        rg1 = float(request.POST.get('rg1'))
        rg2 = float(request.POST.get('rg2'))
        fg = float(request.POST.get('fg'))
        # tg = request.POST.get('tg')
        score_item = get_object_or_404(Score, pk =id)
        score_item.regular_grade1 = rg1
        score_item.regular_grade2 = rg2
        score_item.final_grade = fg

        course_id = request.POST['course_id']
        course = get_object_or_404(Course, pk = course_id)
        rg1_pro = course.regular_proportion1
        rg2_pro = course.regular_proportion2
        fg_pro = course.final_proportion
        tg = rg1 * rg1_pro + rg2 * rg2_pro + fg * fg_pro
        score_item.total_grade = tg
        score_item.save()

        score_list = Score.objects.filter(course=course)

    else:

        course_id = request.GET.get('course_id')
        course = get_object_or_404(Course, pk=course_id)
        score_list = Score.objects.filter(course = course)

    return render(request, 'rms/score_list.html', {'score_list': score_list, 'course': course})


# def print_action(request):


def excel_export(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(User, pk = request.user.pk)
        if user.type == 'student':
            student_id = pk
            student = get_object_or_404(User, pk = student_id)
            score_list = Score.objects.filter(student = student)
            file_name = str(student.sno) + '_' + str(student.username) + '_成绩单.xls'
            print(file_name)
            response = write_to_excel_student(score_list, file_name, student)
            return response

        elif user.type == 'teacher':
            course_id = pk
            course = get_object_or_404(Course, pk = course_id)
            score_list = Score.objects.filter(course = course)
            file_name = str(course.pk) + '_' + str(course.name) + '_学生成绩单.xls'
            print(file_name)
            response = write_to_excel_teacher(score_list, file_name, course)
            return response


# def pdf_export(request, pk):
#     if request.method == 'POST':
#         user = get_object_or_404(User, pk=request.user.pk)
#         if user.type == 'student':
#             student_id = pk
#             student = get_object_or_404(User, pk=student_id)
#             score_list = Score.objects.filter(student=student)
#             file_name = str(student.sno) + '_' + str(student.username) + '成绩单.xls'
#             print(file_name)
#             response = write_to_pdf_student(score_list, file_name, student)
#             return response
#
#         elif user.type == 'teacher':
#             course_id = pk
#             course = get_object_or_404(Course, pk=course_id)
#             score_list = Score.objects.filter(course=course)
#             file_name = str(course.pk) + '_' + str(course.name) + '_学生成绩单.xls'
#             print(file_name)
#             response = write_to_pdf_teacher(score_list, file_name, course)
#             return response




def task_action(request):
    if request.method == 'POST':
        course_list = Course.objects.filter(teacher_id=request.user.pk)
        task_id = request.POST.get('task_id')
        if task_id:
            task_obj = get_object_or_404(Task, pk = task_id)

            form = TaskForm(request.POST or None, request.FILES or None, instance=task_obj)
        else:
            form = TaskForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            task = form.save(commit=False)
            list = request.POST.getlist('checkbox_upload')
            if len(list) != 0:
                task.is_allow_upload = True

            task.author_id = request.user.pk
            task.deadline_time = request.POST.get('deadline_time')
            course_id = request.POST.get('course')
            task.course_id = course_id
            task.save()

            score_list = Score.objects.filter(course_id = course_id)
            student_id_list = []
            for score in score_list:
                student_id_list.append(score.student_id)
            for student_id in student_id_list:
                if len(TaskScore.objects.filter(Q(student_id=student_id)&Q(task=task))) == 0:
                    TaskScore.objects.create(student_id = student_id, task = task).save()


            return redirect('rms:task_list')


    else:
        course_list = Course.objects.filter(teacher_id = request.user.pk)
        task_id = request.GET.get('task_id')
        if task_id:
            t = get_object_or_404(Task, pk = task_id)
            form = TaskForm(instance=t)
            return render(request, 'rms/task_form.html', {'form': form, 'task': t, 'course_list': course_list})
        else:
            form = TaskForm()

    return render(request, 'rms/task_form.html', {'form': form, 'course_list': course_list})


def download_task_file(request, pk):
    task_obj = get_object_or_404(Task, pk = pk)
    file_path = str(settings.MEDIA_URL) + '/' + str(task_obj.appendix)
    file_name = file_path.split('/')[-1]
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(urlquote(file_name))
    return response



def task_delete(request, pk):
    Task(pk = pk).delete()
    return redirect('rms:task_list')



def task_score_action(request):
    if request.method == 'POST':
        taskscore_id = request.POST.get('taskscore_id')
        grade = request.POST.get('grade')
        task_id = request.POST.get('task_id')
        taskscore_obj = get_object_or_404(TaskScore, pk = taskscore_id)
        task_obj = get_object_or_404(Task, pk = task_id)
        taskscore_obj.score = grade
        if taskscore_obj.is_complete == False:
            taskscore_obj.is_complete = True
            task_obj.increase_complete_num()

        taskscore_obj.save()



        taskscore_list = TaskScore.objects.filter(task_id = task_id)


    else:
        task_id = request.GET.get('task_id')
        taskscore_list = TaskScore.objects.filter(task_id = task_id)


    return render(request, 'rms/task_score_list.html', {'tasksocre_list': taskscore_list, 'task_id': task_id})



def task_submit(request, pk):
    if request.method == 'POST':
        # file = request.FILES.get('file')
        # TaskScore.objects.filter(pk = pk).update(file = file, is_complete = True)
        taskscore_obj = get_object_or_404(TaskScore, pk = pk)

        form = TaskSubmitForm(request.POST or None, request.FILES or None, instance = taskscore_obj)
        if form.is_valid():
            task_score = form.save(commit = False)
            task_score.is_complete = True
            task_score.save()

            task_obj = get_object_or_404(Task, pk = taskscore_obj.task_id)
            task_obj.increase_complete_num()

        return redirect('rms:task_list')


    else:
        taskscore_obj = get_object_or_404(TaskScore, pk = pk)
        form = TaskSubmitForm(instance = taskscore_obj)

        return render(request, 'rms/task_submit_form.html', {'form': form, 'taskscore_id': pk})



def download_tasks_submit(request, pk):
    task_obj = get_object_or_404(Task, pk = pk)
    rootdir = str(settings.MEDIA_URL) + '/tasks_submit/' + str(pk)
    the_file_name = '学生任务提交_' + str(task_obj.name) + '.zip'
    z = zipfile.ZipFile(the_file_name, 'w', zipfile.ZIP_DEFLATED)
    for parent,dirnames,filenames in os.walk(rootdir):
        for file in filenames:
            z.write(rootdir + os.sep + file)
    z.close()
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/zip'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(urlquote(the_file_name))
    return response

def file_iterator(file_name, chunk_size=512):
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

