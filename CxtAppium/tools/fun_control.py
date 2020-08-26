#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import time
import csv

class FunControl(object):
    def fun_data(self):
        alldata = [("native", "dalvik","TOTAL")]
        # 设置循环次数
        count = 10
        while count > 0:
            lines = os.popen("adb shell dumpsys meminfo com.immomo.momo")    # adb 查看app内存
            result = lines.read()
            temp = ','.join(result.split())
            native_heap = temp.split('Native,Heap')[1].split(',')[1]
            print ("native_heap:" + str(native_heap))
            dalvik_heap = temp.split('Dalvik,Heap')[1].split(',')[1]
            print ("dalvik_heap:" + str(dalvik_heap))
            total = temp.split('TOTAL')[1].split(',')[1]
            print ("total:" + str(total))
            alldata.append([native_heap, dalvik_heap,total])
            count -= 1
            print('还剩余：%s次'%count)
            time.sleep(1)   # 等待时间
            csvfile = open('../data/function.csv', 'w',encoding='utf8',newline='')
            writer = csv.writer(csvfile)
            writer.writerows(alldata)
            csvfile.close()