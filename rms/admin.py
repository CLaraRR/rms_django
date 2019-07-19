from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'found_time', 'location')


class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'found_time', 'institute')


class SectionInfoAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'institute', 'major', 'student_num')


class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'sno', 'section_info', 'type', 'sex', 'birthday')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),

        (gettext_lazy('User Information'), {'fields': ('sno', 'section_info', 'type', 'sex', 'birthday')}),

        (gettext_lazy('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                                  'groups', 'user_permissions')}),

        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'total_hours', 'credit', 'teacher', 'institute')

# class Score(admin.ModelAdmin):
#     list_display = ('course', 'student', 'total_grade' )



admin.site.register(Institute, InstituteAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(SectionInfo, SectionInfoAdmin)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Course, CourseAdmin)

# admin.site.register(Score)
