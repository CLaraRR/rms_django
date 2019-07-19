from xlwt import *
from io import BytesIO
from comtypes.client import CreateObject
from comtypes import CoInitialize
from reportlab.pdfgen import canvas
import os
from win32com.client import Dispatch, constants, gencache, DispatchEx
from django.http import HttpResponse, FileResponse
from django.utils.encoding import escape_uri_path
from django.conf import settings


def write_to_excel_student(score_list, file_name, student):
    if score_list:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet("sheet1")

        w.write(0, 0, u"学号")
        w.write(0, 1, u"姓名")
        w.write(0, 2, u"学院")
        w.write(0, 3, u"专业")
        w.write(0, 4, u"入学年份")

        w.write(1, 0, student.sno)
        w.write(1, 1, student.username)
        w.write(1, 2, student.section_info.institute.name)
        w.write(1, 3, student.section_info.major.name)
        w.write(1, 4, student.section_info.year)

        w.write(3, 0, u"序号")
        w.write(3, 1, u"课程编号")
        w.write(3, 2, u"课程名称")
        w.write(3, 3, u"学分")
        w.write(3, 4, u"开办学院")
        w.write(3, 5, u"平时成绩1")
        w.write(3, 6, u"平时成绩2")
        w.write(3, 7, u"期末成绩")
        w.write(3, 8, u"总成绩")
        # 写入数据
        row = 4
        for score in score_list:
            w.write(row, 0, row)
            w.write(row, 1, score.course.pk)
            w.write(row, 2, score.course.name)
            w.write(row, 3, score.course.credit)
            w.write(row, 4, score.course.institute.name)
            w.write(row, 5, score.regular_grade1)
            w.write(row, 6, score.regular_grade2)
            w.write(row, 7, score.final_grade)
            w.write(row, 8, score.total_grade)
            row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        # exist_file = os.path.exists(file_name)
        # if exist_file:
        #     os.remove(file_name)
        # ws.save(file_name)
        ############################
        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse()
        response['Content-Type'] = 'application/vnd.ms-excel'
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
        response.write(sio.getvalue())
        return response



def write_to_excel_teacher(score_list, file_name, course):
    if score_list:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet("sheet1")
        w.write(0, 0, u"课程编号")
        w.write(0, 1, u"课程名称")
        w.write(0, 2, u"学分")
        w.write(0, 3, u"开办学院")
        w.write(0, 4, u"任课教师")

        w.write(1, 0, course.pk)
        w.write(1, 1, course.name)
        w.write(1, 2, course.credit)
        w.write(1, 3, course.institute.name)
        w.write(1, 4, course.teacher.username)

        w.write(3, 0, u"序号")
        w.write(3, 1, u"学生姓名")
        w.write(3, 2, u"学号")
        w.write(3, 3, u"平时成绩1")
        w.write(3, 4, u"平时成绩2")
        w.write(3, 5, u"期末成绩")
        w.write(3, 6, u"总成绩")
        # 写入数据
        row = 4
        for score in score_list:
            w.write(row, 0, row - 1)
            w.write(row, 1, score.student.username)
            w.write(row, 2, score.student.sno)
            w.write(row, 3, score.regular_grade1)
            w.write(row, 4, score.regular_grade2)
            w.write(row, 5, score.final_grade)
            w.write(row, 6, score.total_grade)
            row += 1
        # 检测文件是够存在
        # 方框中代码是保存本地文件使用，如不需要请删除该代码
        ###########################
        # exist_file = os.path.exists(file_name)
        # if exist_file:
        #     os.remove(file_name)
        # ws.save(file_name)
        ############################

        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse()
        response['Content-Type'] = 'application/vnd.ms-excel'
        response['Content-Disposition'] = "attachment;filename*=utf-8''{}".format(escape_uri_path(file_name))
        response.write(sio.getvalue())
        return response






# def write_to_pdf_teacher(score_list, file_name, course):
#     if score_list:
#         # 创建工作薄
#         ws = Workbook(encoding='utf-8')
#         w = ws.add_sheet("sheet1")
#         w.write(0, 0, u"课程编号")
#         w.write(0, 1, u"课程名称")
#         w.write(0, 2, u"学分")
#         w.write(0, 3, u"开办学院")
#         w.write(0, 4, u"任课教师")
#
#         w.write(1, 0, course.pk)
#         w.write(1, 1, course.name)
#         w.write(1, 2, course.credit)
#         w.write(1, 3, course.institute.name)
#         w.write(1, 4, course.teacher.username)
#
#         w.write(3, 0, u"序号")
#         w.write(3, 1, u"学生姓名")
#         w.write(3, 2, u"学号")
#         w.write(3, 3, u"平时成绩1")
#         w.write(3, 4, u"平时成绩2")
#         w.write(3, 5, u"期末成绩")
#         w.write(3, 6, u"总成绩")
#         # 写入数据
#         row = 4
#         for score in score_list:
#             w.write(row, 0, row - 1)
#             w.write(row, 1, score.student.username)
#             w.write(row, 2, score.student.sno)
#             w.write(row, 3, score.regular_grade1)
#             w.write(row, 4, score.regular_grade2)
#             w.write(row, 5, score.final_grade)
#             w.write(row, 6, score.total_grade)
#             row += 1
#
#         exist_file = os.path.exists(file_name)
#         if exist_file:
#             os.remove(file_name)
#         ws.save(file_name)
#
#         file_path = os.path.join(settings.BASE_DIR, file_name)
#         pdf_path = file_path.replace('xls', 'pdf')
#         pdf_name = file_name.replace('xls', 'pdf')
#         # xlApp = CreateObject("Excel.Application")
#         xlApp = DispatchEx("Excel.Application")
#         xlApp.Visible = False
#         xlApp.DisplayAlerts = 0
#         books = xlApp.Workbooks.Open(file_path, False)
#         books.ExportAsFixedFormat(0, pdf_path)
#         books.Close(False)
#         xlApp.Quit()
#
#         file = open(pdf_path, 'rb')
#         response = FileResponse(file)
#         response['Content-Type'] = 'application/octet-stream'
#         response['Content-Disposition'] = 'attachment;filename="{0}"'.format(pdf_name)
#         return response
#
#
# def write_to_pdf_student(score_list, file_name, student):
#     if score_list:
#         # 创建工作薄
#         ws = Workbook(encoding='utf-8')
#         w = ws.add_sheet("sheet1")
#
#         w.write(0, 0, u"学号")
#         w.write(0, 1, u"姓名")
#         w.write(0, 2, u"学院")
#         w.write(0, 3, u"专业")
#         w.write(0, 4, u"入学年份")
#
#         w.write(1, 0, student.sno)
#         w.write(1, 1, student.username)
#         w.write(1, 2, student.section_info.institute.name)
#         w.write(1, 3, student.section_info.major.name)
#         w.write(1, 4, student.section_info.year)
#
#         w.write(3, 0, u"序号")
#         w.write(3, 1, u"课程编号")
#         w.write(3, 2, u"课程名称")
#         w.write(3, 3, u"学分")
#         w.write(3, 4, u"开办学院")
#         w.write(3, 5, u"平时成绩1")
#         w.write(3, 6, u"平时成绩2")
#         w.write(3, 7, u"期末成绩")
#         w.write(3, 8, u"总成绩")
#         # 写入数据
#         row = 4
#         for score in score_list:
#             w.write(row, 0, row)
#             w.write(row, 1, score.course.pk)
#             w.write(row, 2, score.course.name)
#             w.write(row, 3, score.course.credit)
#             w.write(row, 4, score.course.institute.name)
#             w.write(row, 5, score.regular_grade1)
#             w.write(row, 6, score.regular_grade2)
#             w.write(row, 7, score.final_grade)
#             w.write(row, 8, score.total_grade)
#             row += 1
#
#         exist_file = os.path.exists(file_name)
#         if exist_file:
#             os.remove(file_name)
#         ws.save(file_name)
#
#         file_path = os.path.join(settings.BASE_DIR, file_name)
#         pdf_path = file_path.replace('xls', 'pdf')
#         pdf_name = file_name.replace('xls', 'pdf')
#         # CoInitialize()
#         xlApp = CreateObject("Excel.Application")
#         books = xlApp.Workbooks.Open(file_name)
#         books.ExportAsFixedFormat(0, pdf_path)
#         xlApp.Quit()
#
#         file = open(pdf_path, 'rb')
#         response = FileResponse(file)
#         response['Content-Type'] = 'application/octet-stream'
#         response['Content-Disposition'] = 'attachment;filename="{0}"'.format(pdf_name)
#         return response