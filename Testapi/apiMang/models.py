from django.db import models

# Create your models here.
class project(models.Model):
    '''project表创建'''
    project_name = models.CharField(max_length=20)
    version = models.IntegerField(max_length=10)
    ctime = models.DateTimeField()
    utime = models.DateTimeField()
    status = models.IntegerField(max_length=10)

class member(models.Model):
    '''成员表创建'''
    member_name = models.CharField(max_length=20)
    sex = models.IntegerField(max_length=10)
    status = models.IntegerField(max_length=10)
    project_id = models.ForeignKey(project,on_delete=models.CASCADE)    #外键关联
    phone = models.IntegerField(max_length=100)
    power = models.CharField(max_length=20)
    e_mail = models.CharField(max_length=20)
    ctime = models.DateTimeField()
    utime = models.DateTimeField()

class case(models.Model):
    '''用例表创建'''
    case_name = models.CharField(max_length=20)
    project_id = models.ForeignKey(project,on_delete=models.CASCADE)  #外键关联
    request = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    parameter = models.CharField(max_length=1000)
    u_member = models.CharField(max_length=10)
    expect_result = models.CharField(max_length=100)
    reality_result = models.CharField(max_length=1000)
    result = models.CharField(max_length=10)
    status = models.IntegerField(max_length=10)
    ctime = models.DateTimeField()
    utime = models.DateTimeField()

class project_log(models.Model):
    '''项目操作日志'''
    op_project = models.ForeignKey(project,on_delete=models.CASCADE)  # 外键关联
    op_time = models.DateTimeField()
    op_type = models.CharField(max_length=10)
    op_member = models.CharField(max_length=10)
    op_show = models.CharField(max_length=10)
    status = models.IntegerField(max_length=10)

class test_report(models.Model):
    '''测试报告表'''
    op_project = models.ForeignKey(project,on_delete=models.CASCADE)  # 外键关联
    pass_num = models.IntegerField(max_length=5)
    fail_num = models.IntegerField(max_length=5)
    error_num = models.IntegerField(max_length=5)
    test_time = models.IntegerField(max_length=10)
    ctime = models.IntegerField(max_length=10)
    status = models.IntegerField(max_length=10)
