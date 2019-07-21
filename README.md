# ResourceManagementSystem2.0(教学资源管理系统2.0)

标签： python django

---


本项目是教学资源管理系统的2.0版本，采用Python和Django进行编写，1.0版本在https://github.com/CLaraRR/Resource-Management-System 可以找到，采用Java实现。本项目使用的前端模板是从网上搜集而来，可以从另一个repo下载https://github.com/CLaraRR/BackgroundManagementSystem-template 。

---
2.0版本相对于1.0版本的实现除了使用语言不同之外，还增加了几个模块，下面是这个项目的介绍。

---
## 一、运行项目
clone或下载项目到本地，建议在虚拟环境下运行该项目。

### 1.建立虚拟环境

Ctrl + R打开cmd,输入
```
pip install virtualenv
```

创建一个文件夹专门用来存放虚拟环境，比如F:\PythonEnvs，进入该文件夹下，打开命令行，输入
```
virtualenv rms_env
```

然后rms_env文件夹就会被创建了，进入到Scripts文件夹，命令行输入
```
./activate
```

看到命令行前面多出了（rms_env）意思就是进入了我们刚才创建的虚拟环境

往后运行项目都在这个虚拟环境下，如果没看到前面的（rms_env）则按上面的方法重新进入。

### 2.安装所需的第三方库
在这个虚拟环境下进入到这个项目的根目录，命令行输入
```
pip install -r requirements.txt
```
然后就会自动安装所需的库了

mysqlclient在windows可能会安装失败，可以通过whl安装，在mysqlclient文件夹可以找到（因为我的平台是win10，所以我只下载了windows版本的whl，版本有27、37、38），根据自己的python的版本选择，然后命令行输入
```
pip install whl所在路径
```

### 3.迁移数据库
在mysql数据库新建名为rms的数据库，在项目rms_django文件夹下的setting.py中修改数据库账号密码为你自己的数据库账号密码。

迁移数据库至mysql:命令行输入
```
python manage.py makemigrations
python manage.py migrate
```
django就会自动在数据库里面建立model.py的类所对应的表。

### 4.运行项目
在这个虚拟环境下进入到这个项目的根目录，命令行输入
```
python manage.py runserver

```

启动服务器成功后打开浏览器，输入http://127.0.0.1:8000/login/ 就能看到项目的登录页面了。

因为此时数据库里面还没有任何用户，而一般系统都会有一个超级用户，也就是管理员，所以先创建一个超级用户,，命令行输入
```
python manage.py create superuser
```

根据提示填写管理员信息。

创建好管理员之后，在浏览器输入http://127.0.0.1:8000/admin/ ，用刚才创建的账号密码登录，这就进入了django自带的管理后台。在这个后台可以直接对各个用户进行设置，也可以对各个model进行增删查改。

我们可以在管理后台创建一些教师、学生用户，也可以创建学院、专业、课程的数据。

如果不想自己一个个创建，可以参考我的数据库，里面已经创建好了一些数据段，在mydatabase文件夹可以找到，用mysql管理工具就可以导入数据。

*ps:我只提供了某些表的数据，像resource表或者与resource表关联的表的数据我没有提供，因为resource需要用户在系统内上传资源才会在表中创建字段，这个大家就自行添加啦。*


## 二、功能介绍
这个教学资源管理系统（以下简称为rms）主要面向学校的三类用户：管理员、教师、学生，主要功能有用户管理、课程管理、课程成绩管理、资源管理、举报管理、通知管理、任务管理、任务成绩管理等。

## 三、模块介绍
各类用户在不同模块中的操作不同。

| 模块 | 管理员   | 教师    | 学生 |
| ---- | -------- | ------- | -------- |
| 用户管理 | 对各类用户增删查改 | - | - |
| 课程管理 | 对课程增删查改 | 查 | 查|
| 课程成绩管理| 对课程成绩增删查改 | 增删查改 | 查|
| 资源管理 | 对资源增删查改 | 增查 | 增查|
| 举报管理 | 对举报删查 | 增查 | 增查 |
| 通知管理 | 对通知增删查改 | 查 | 查 |
| 任务管理 | 对任务增删查改 | 增删查改 | 查 |
| 任务成绩管理| 对任务成绩增删查改 | 增删查改 | 查 |



## 四、models.py数据模型介绍
以下模型在migrate时都在数据库自动创建了id字段，并自动设置为主键，因此下面在表格中省略书写id字段。
### 1.Institute model学院模型

| 字段名称 | 含义 | 类型 |
| ----- | ----- | ----- | 
| name | 学院名称 | CharField | 
| found_time | 成立时间 | DateField | 
| location | 所在地址 | TextField |
| teacher_num | 教师人数 | PositiveIntegerField |

模型操作：increase_teacher_num 每增加一个教师用户则教师人数加1

### 2.Major model专业模型

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
| name | 专业名称 | CharField |
| found_time | 成立日期 | DateField | 
| institute | 所在学院 | ForeignKey：Institute |

### 3.SectionInfo model部门信息模型
以 某入学年份+某入学学期+某学院机构+某专业 作为一个部门单位

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
| year | 入学年份|CharField|
| semester |入学学期|CharField|
|institute|学院|ForeignKey:Institute|
|major|专业|ForeignKey:Major|
|student_num|部门学生人数|PositiveIntegerField|

模型操作：increase_student_num 每增加一个学生用户，该学生用户所在部门的学生总人数加1

### 4.User model用户模型
该用户模型可包含管理员、教师、学生三类用户

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|sno|学工号|CharField|
|section_info|所在部门|ForeignKey：SectionInfo|
|sex|性别|CharField|
|birthday|出生日期|DateField|
|type|用户类型|CharField|

*说明：sno根据用户所在部门信息自动生成，无需手动设置。type有3种类型分别对应admin, teacher, student*

### 5.Course model课程模型

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|课程名称|CharField|
|create_time|创建时间|DateField|
|total_hours|总学时|PositiveIntegerField|
|credit|学分|PositiveIntegerField|
|teacher|任课教师|ForeignKey:User,limit_choices_to={'type':'teacher'}
|institute|开办学院|ForeignKey:Institute|
|regular_proportion1|平时成绩1占比|FloatField|
|regular_proportion2|平时成绩2占比|FloatField|
|final_proportion|期末成绩占比|FloatField|

*说明：teacher字段是一个外键，指向的是User表，且限制用户类型为teacher*

### 6.Score model课程成绩模型
修读某一门课程的学生将自动为其增加一条score记录

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|course|课程名称|ForeignKey：Course|
|student|学生|ForeignKey:User|
|regular_grade1|平时成绩1|FloatField|
|regular_grade2|平时成绩2|FloatField|
|final_grade|期末成绩|FloatField|
|total_grade|总成绩|FloatField|
|credit|获得学分绩点|PositiveIntegerField|

### 7.Task model任务模型
| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|任务标题|CharField|
|course|课程名称|ForeignKey:Course|
|description|描述|TextField|
|content|内容|TextField|
|is_allow_upload|是否要求上传附件|BooleanField|
|create_time|创建时间|DateTimeField|
|modify_time|修改时间|DateTimeField|
|deadline_time|提交截止日期|DateTimeField|
|author|作者|ForeignKey:User|
|appendix|附件|FileField|
|complete_num|完成人数|PositiveIntegerField|
|views|浏览数|PositiveIntegerField|

模型操作：

1.increase_views 任务页面每一打开一次浏览数加1

2.increase_complete_num 任务可以要求学生上传作业或者不上传，若要求学生上传作业，则当学生上传了作业则完成人数自动加1；若不要求学生上传作业，则由老师自行确认学生是否完成作业，老师在给学生打分时将默认为该学生完成作业，并且完成人数加1

### 8.TaskScore model任务成绩模型
修读了某一门课程的学生，当该门课的任课老师布置一个任务时，将自动为这个学生增加一条关于这个任务的score记录

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|task|所在任务|ForeignKey:Task|
|student|学生|ForeignKey:User|
|file|作业文件|FileField|
|is_complete|是否完成任务|BooleanField|
|score|任务成绩|PositiveIntegerField|

### 9.Notice model通知模型
| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|通知标题|CharField|
|content|通知内容|TextField|
|create_time|创建时间|DateTimeField|
|modify_time|修改时间|DateTimeField|
|file|附件|FileField|
|author|作者|CharField|
|views|浏览数|PositiveIntegerField|
|downloads|附件下载次数|PositiveIntegerField|

模型操作：

1.increase_views 通知页面每被浏览一次则浏览数加1

2.increase_downloads 通知附件每被下载一次则下载数加1

### 10.Report model举报信息模型
用户可以对资源进行举报

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|举报标题|CharField|
|resource|举报资源|ForeignKey:Resource|
|description|描述|TextField|
|content|详细举报内容|TextField|
|create_time|创建时间|DateTimeField|
|author|举报人|ForeignKey:User|
|is_view|管理员是否已查看该举报|BooleanField|
|is_manage|管理员是否已处理该举报|BooleanField|

模型操作：

1.view_status 如果管理员查看了该举报信息，则is_view字段变为true

2.manage_status 如果管理员处理了该举报信息，则is_manage字段变为true

### 11.Category model资源类别模型
| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|资源类别|CharField|

### 12.Resource model资源模型
用户可以上传资源至rms

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|name|资源名称|CharField|
|description|描述|TextField|
|category|类别|ForeignKey:Category|
|version|版本|CharField|
|author|作者|CharField|
|file|资源文件|FileField|
|image|资源图标|ImageField|
|create_time|创建时间|DateTimeField|
|views|资源浏览数|PositiveIntegerField|
|downloads|资源下载数|PositiveIntegerField|

模型操作：

1.increase_views 资源页面每被浏览一次则浏览数加1

2.increase_downloads 资源每被下载一次则下载数加1

### 13.Comment model评论模型
用户可以对资源进行评论

| 字段名称 | 含义 | 类型 | 
| ----- | ----- | ----- | 
|resource|评论的资源|ForeignKey:Resource|
|content|评论的内容|TextField|
|author|作者|CharField|
|create_time|创建时间|DateTimeField|



## 五、views.py实现的功能介绍
### 一、一些View
这些View是用class体现的。具体含义我就不一一解释了，应该从字面上就能看出来是干嘛的，主要就是从数据库取出数据到模板页面显示，不参与数据的post和get。

|IndexView|ResourceView|CategoryView|NoticeListView|
| --- | --- | --- | --- |
|ProfileView|ReportListView|ReportDetialView|CourseListView|
|ScoreListView|TaskListView|TaskDetailView|


### 二、一些相关的action
这些action是用函数体现的。

|函数名|所属模块|作用|
| --- | ------- | - |
|download_resource|资源管理|下载资源|
|resource_action|资源管理|GET:获取资源信息表单渲染至模板;POST:获取表单数据并上传资源|
|report_action|举报管理|GET:获取举报信息表单渲染至模板；POST:获取表单字段数据保存至数据库|
|report_manage|举报管理|修改举报信息“是否已处理”状态|
|report_delete|举报管理|删除举报数据|
|notice_action|通知管理|GET:获取通知表单渲染至模板；POST：获取表单数据保存至数据库|
|download_notice|通知管理|下载通知附件|
|course_action|课程管理|GET:获取课程信息表单；POST：提交课程信息表单|
|course_delete|课程管理|删除课程数据|
|course_student|课程成绩管理|GET:获取修读该门课的学生列表；POST：添加/更新修读该门课的学生，在Score表添加/更新该学生对应课程的成绩数据段|
|course_equation|课程管理|GET:获得该门课的成绩计算公式；POST:更新该门课的成绩计算公式|
|score_action|课程成绩管理|GET:获得某门课所有学生的成绩列表；POST:添加/更新该门课某个学生的成绩|
|excel_export|课程成绩管理|导出成绩单为excel格式并下载到本地|
|task_action|任务管理|GET:获取任务信息表单；POST：添加/更新任务信息|
|download_task_file|任务管理|下载任务附件|
|task_delete|任务管理|删除某任务数据|
|task_score_action|任务成绩管理|GET:获取某任务所有学生的成绩列表；POST:添加/更新某学生的任务成绩|
|task_submit|任务成绩管理|GET:获取某任务的提交表单；POST：学生提交任务，添加/更新任务成绩数据|
|download_tasks_submit|任务管理|教师可以下载某个任务下所有学生提交的文件|

## 六、forms.py定义的表单概览
django会根据定义好的form的字段自动在模板渲染该字段域，在后台通过form可获得对应model的对象。

|表单|fileds|
| --- | --- |
|ReportForm|name, description, content|
|ResourceForm|name, description, category, version, author, file, image|
|CommentForm|content, author|
|NoticeForm|name, content, file, author|
|CourseForm|name, create_time, total_hours, credit, teacher, institute|
|TaskForm|name, description, content, appendix|
|TaskSubmitForm|file|

因为我在实现form的时候是继承forms.ModelForm的，所以一个form对应一个model，form的fields其实是对应model的字段，在后台可以通过form = XXForm(request.POST)获取到表单数据，然后通过form.save()可以直接创建model对象并持久化到数据库。但是有些字段我没有放在在form里面，他就不会在模板自动渲染，因此在后台也不会获取到这些字段的数据，所以如果我要获得这些字段的数据的话可以用一般的html标签在模板定义一个输入域，如`<input/>`，然后在后台通过value = request.POST.get('name')得到该字段对应的数据。






