from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import case
from apiMang.models import project
from apiMang.models import test_report
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return render(request, "index.html")

def  login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登陆
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/api_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

'''
# 接口管理
@login_required
def api_manage(request):
    api_list = case.objects.all()
    username = request.session.get('username', '')
    return render(request, "api_manage.html", {"user": username, "apis": api_list})
'''
# 用例—分页
#@login_required
def api_manage(request):
    api_list = case.objects.all()
    username = request.session.get('username', '')
    paginator = Paginator(api_list, 2)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "api_manage.html", {"user": username, "apis": contacts})

# 用例名称搜索
#@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("case_name", "")
    event_list = case.objects.filter(case_name__contains=search_name)
    return render(request, "api_manage.html", {"user": username,"apis": event_list})

#项目管理
#@login_required
def project_manage(request):
    username = request.session.get('user', '')
    project_list = project.objects.all()
    return render(request, "project_manage.html", {"user": username,"projects": project_list})

#报告管理
#@login_required
def report_manage(request):
    username = request.session.get('user', '')
    report_list = test_report.objects.all()
    paginator = Paginator(report_list, 1)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "report_manage.html", {"user": username, "reports": contacts})

# 退出登录
#@login_required
def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/index/')
    return response
