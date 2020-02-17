#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from common.op_yaml import OperationYaml
from common.runmethod import RunMethon
from common.op_data import OperationData
from common.logger import Log

class TestOne():
    def __init__(self):
        self.data = OperationData()
        self.data.op_data('test1')  #需要请求地址和方法

        self.ya = OperationYaml('test1')
        self.run = RunMethon()
        self.log = Log()

    def testLogistics(self):
        self.log.info('-----开始执行第一个文件，第一个用例-----')
        data = self.ya.get_data('test1_1')
        rel = self.run.run_main(self.data.method[0],self.data.url[0],data)

        print(rel)
        return rel

    def testLongude(self):
        self.log.info('-----开始执行第一个文件，第二个用例-----')
        data = self.ya.get_data('test1_2')
        rel = self.run.run_main(self.data.method[1],self.data.url[1],data)
        print(rel)
        return rel


if __name__ == '__main__':
    re = TestOne()
    re.testLogistics()
