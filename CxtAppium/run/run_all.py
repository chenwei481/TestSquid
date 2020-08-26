#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import unittest
import time,logging
import sys
path='../CxtAppium'
sys.path.append(path)
from tools.HTMLTestRunner import HTMLTestRunner
from tools.opExcel import OperationExcel as opEx

#定义测试用例和测试报告的路径
test_dir='../test_case'
report_dir='../results/reports'

data = opEx()
lines = data.get_lines()
for i in range(1,lines):
    is_run = data.get_cell_value(i,1)
    if is_run == 'yes':
        case_name = data.get_cell_value(i,0)
        print(case_name)

        #加载测试用例
        discover=unittest.defaultTestLoader.discover(test_dir,pattern='%s'%case_name)

        #加载全部测试用例
        #discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

        now=time.strftime('%Y-%m-%d %H-%M-%S')
        filepath=report_dir+'/'+now+' testReport.html'
        with open(filepath,'wb') as f:
            runner=HTMLTestRunner(stream=f,title='测试报告',description='TestReport')
            logging.info('测试开始')
            runner.run(discover)