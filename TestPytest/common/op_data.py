#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from common.op_excel import OperationExcel

class OperationData():
    def op_data(self,file):
        op_ex = OperationExcel('%s' %file,0)
        allline = op_ex.get_lines()

        allurl = []
        allmethod = []
        allexile = []
        for i in range(1, allline):
            url = op_ex.get_cell_value(i, 3)
            allurl.append(url)
            method = op_ex.get_cell_value(i, 5)
            allmethod.append(method)
            exile = op_ex.get_cell_value(i, 7)
            allexile.append(exile)
        self.url = allurl
        self.method = allmethod
        self.exile = allexile

if __name__ == '__main__':
    res = OperationData()
    res.op_data('test2')
