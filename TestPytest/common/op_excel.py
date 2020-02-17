#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class OperationExcel:
        def __init__(self,file_address=None,sheet_id=None):
                if file_address != None:                          #条件判断输入时是否传地址，如果传了地址就执行if下面语句，单独赋值
                        self.file_address = '../testdata/excel/%s.xlsx'%file_address
                        self.sheet_id = sheet_id
                else:                                             #如果没有传地址，就执行else操作，赋Excel地址和sheet_id
                        print('没有传Excel文件名')

                self.data = self.get_data()

        def get_data(self):
                '''获取sheets的内容'''
                data = xlrd.open_workbook(self.file_address)         #打开文件
                tables = data.sheets()[self.sheet_id]                #获取文件内容
                return tables

        def get_lines(self):
                '''获取单元格行数'''
                tables = self.data                    #把文件内容赋予tables
                return tables.nrows

        def get_cell_value(self,row,col):
                '''获取某一单元格内容'''
                return self.data.cell_value(row,col)       #根据行列返回表单内容

        def write_value(self,row,col,value):
                '''写入数据'''
                read = xlrd.open_workbook(self.file_address)
                write_data = copy(read)
                sheet_data = write_data.get_sheet(0)
                sheet_data.write(row, col, value)
                write_data.save(self.file_address)


if __name__ == '__main__':
        opers = OperationExcel('test1',0)
        #print(opers.__init__('F:\TestRobt2.0\Addguest1.xlsx',0))
        print(opers.get_cell_value(0,3))
