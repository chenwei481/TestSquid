#author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.http import JsonResponse
from .models import test_report,project,case
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
import time

# 添加用例接口
def add_case(request):
    id = request.POST.get('id','')
    case_name = request.POST.get('case_name','')
    requests = request.POST.get('request','')
    url = request.POST.get('url','')
    parameter = request.POST.get('parameter','')
    u_member = request.POST.get('u_member','')
    expect_result = request.POST.get('expect_result', '')
    reality_result = request.POST.get('reality_result', '')
    result = request.POST.get('result', '')
    statuss = request.POST.get('status', '')
    ctime = request.POST.get('ctime', '')
    utime = request.POST.get('utime', '')
    project_id_id = request.POST.get('project_id_id', '')
    if case_name == '' or requests == '' or url == '' or parameter == '' or expect_result == '' or statuss == '':
        return JsonResponse({'status':10021,'message':'参数错误'})

    result = case.objects.filter(id = id)
    if result:
        return JsonResponse({'status':10022,'message':'id已经存在'})

    result = case.objects.filter(case_name = case_name)
    if result:
        return JsonResponse({'status':10023,'message':'用例已经存在'})
    if statuss == '':
        status = 1
    try:
        case.objects.create(case_name=case_name,request=requests,url=url,parameter=parameter,expect_result=expect_result,status=statuss)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})
    return JsonResponse({'status':200,'message':'添加用例成功'})
