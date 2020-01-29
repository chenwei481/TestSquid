from django.contrib import admin
from .models import project,project_log,member,case,test_report

class memberInfoLine(admin.TabularInline):
    '''添加关联'''
    model = member
    extra = 1

class projectInfoAdmin(admin.ModelAdmin):
    '''页面展示'''
    list_display = ['id','project_name','version','ctime','utime','status']  #显示库里面的字段展示在页面
    list_filter = ['project_name','version']   #页面添加过滤功能
    search_fields = ['project_name'] #添加页面搜索功能
    inlines = [memberInfoLine]    #建立关联

class memberInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'member_name', 'sex', 'status', 'phone', 'power','e_mail','ctime','utime','project_id_id']  # 显示库里面的字段展示在页面
    list_filter = ['project_id_id', 'member_name']  # 页面添加过滤功能
    search_fields = ['member_name']  # 添加页面搜索功能

class caseInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'case_name', 'request', 'url', 'parameter', 'u_member','expect_result','reality_result','result','utime','project_id_id']  # 显示库里面的字段展示在页面
    list_filter = ['project_id_id', 'case_name']  # 页面添加过滤功能
    search_fields = ['case_name']  # 添加页面搜索功能

class projectLogInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'op_time', 'op_type', 'op_member', 'op_show', 'status','op_project_id']  # 显示库里面的字段展示在页面
    list_filter = ['op_project_id', 'op_type']  # 页面添加过滤功能
    search_fields = ['op_member']  # 添加页面搜索功能

class testReportInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pass_num', 'fail_num', 'error_num', 'test_time', 'ctime','status','op_project_id']  # 显示库里面的字段展示在页面
    list_filter = ['op_project_id']  # 页面添加过滤功能
    search_fields = ['pass_num', 'fail_num', 'error_num']  # 添加页面搜索功能

admin.site.register(project,projectInfoAdmin)
admin.site.register(member,memberInfoAdmin)
admin.site.register(case,caseInfoAdmin)
admin.site.register(project_log,projectLogInfoAdmin)
admin.site.register(test_report,testReportInfoAdmin)
