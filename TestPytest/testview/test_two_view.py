#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from common.op_yaml import OperationYaml
from common.runmethod import RunMethon
from common.op_data import OperationData
from common.logger import Log

class TestTwo():
    def __init__(self):
        self.data = OperationData()
        self.data.op_data('test2')
        self.ya = OperationYaml('test2')
        self.run = RunMethon()
        self.log = Log()

    def testTaobao(self):
        self.log.info('-----开始执行第二个文件，第一个用例-----')
        data = self.ya.get_data('test2_1')
        rel = self.run.run_main(self.data.method[0],self.data.url[0],data)
        print(rel)
        return rel



if __name__ == '__main__':
    re = TestTwo()
    re.testTaobao()