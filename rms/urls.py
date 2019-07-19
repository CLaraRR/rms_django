from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


from . import views


app_name = 'rms'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name = 'index'),
    path('resource_page/<int:pk>/', views.ResourceView.as_view(), name = 'resource_page'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name = 'category'),
    path('download_resource/<int:pk>/', views.download_resource,  name = 'download_resource'),
    path('report_action/<int:pk>/', views.report_action, name = 'report_action'),
    path('upload_resource/', views.resource_action, name = 'upload_resource'),
    path('notice_list/', views.NoticeListView.as_view(), name = 'notice_list'),
    path('notice_page/<int:pk>/', views.NoticeDetialView.as_view(), name = 'notice_page'),
    path('publish_notice/', views.notice_action, name = 'publish_notice'),
    path('download_notice/<int:pk>/', views.download_notice, name = 'download_notice'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name = 'profile'),
    path('report_list/', views.ReportListView.as_view(), name = 'report_list'),
    path('report_page/<int:pk>/', views.ReportDetialView.as_view(), name = 'report_page'),
    path('report_manage/<int:pk>/', views.report_manage, name = 'report_manage'),
    path('report_delete/<int:pk>/', views.report_delete, name = 'report_delete'),
    path('course_list/', views.CourseListView.as_view(), name = 'course_list'),
    path('course_action/', views.course_action, name = 'course_action'),
    path('course_delete/<int:pk>/', views.course_delete, name = 'course_delete'),
    path('course_student/', views.course_student, name = 'course_student'),
    path('course_equation/<int:pk>/', views.course_equation, name = 'course_equation'),
    path('my_score_list/', views.ScoreListView.as_view(), name = 'my_score_list'),
    path('score_list/', views.score_action, name = 'score_list'),
    path('score_action/', views.score_action, name = 'score_action'),
    path('excel_export/<int:pk>/', views.excel_export, name = 'excel_export'),
    # path('pdf_export/<int:pk>/', views.pdf_export, name = 'pdf_export'),
    path('task_list/',views.TaskListView.as_view(), name = 'task_list'),
    path('task_action/', views.task_action, name = 'task_action'),
    path('task_page/<int:pk>/', views.TaskDetailView.as_view(), name = 'task_page'),
    path('download_task_file/<int:pk>/', views.download_task_file, name = 'download_task_file'),
    path('task_delete/<int:pk>/',views.task_delete, name = 'task_delete'),
    path('task_score_action/', views.task_score_action, name = 'task_score_action'),
    path('task_submit/<int:pk>/', views.task_submit, name = 'task_submit'),
    path('download_tasks_submit/<int:pk>/', views.download_tasks_submit, name = 'download_tasks_submit'),




















] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)