#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xlrd
from xlutils.copy import copy

class OperationExcel:
        def __init__(self,file_address=None,sheet_id=None):
                if file_address != None:
                        self.file_address = file_address
                        self.sheet_id = 0
                else:
                        self.file_address = '../data/caselist.xlsx'
                        self.sheet_id = 0

                self.data = self.get_data()

        #获取sheets的内容
        def get_data(self):
                data = xlrd.open_workbook(self.file_address)         #打开文件
                tables = data.sheets()[self.sheet_id]                #获取文件内容
                return tables

        #获取单元格行数
        def get_lines(self):
                tables = self.data                    #把文件内容赋予tables
                return tables.nrows
        
        #获取某一单元格内容
        def get_cell_value(self,row,col):
                return self.data.cell_value(row,col)       #根据行列返回表单内容


        #写入数据
        def write_value(self,row,col,value):
                read = xlrd.open_workbook(self.file_address)
                write_data = copy(read)
                sheet_data = write_data.get_sheet(0)
                sheet_data.write(row, col, value)
                write_data.save(self.file_address)


        #获取某一列的内容
        def get_cols_data(self,col_id = None):
                if col_id != None:
                        cols = self.data.col_value(col_id)
                else:
                        cols = self.data.col_value(0)
                return cols




if __name__ == '__main__':
        opers = OperationExcel()
        #print(opers.__init__('F:\TestRobt2.0\Addguest1.xlsx',0))
        print(opers.get_cell_value(1,3))
