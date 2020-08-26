#Author:chen
#!/usr/bin/env python
#-*-coding:gb2312-*-
from tools.baseLocation import BaseLocation
import logging
from tools.desired_caps import appium_desired
import time,os
import csv
from config.setting import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Common(BaseLocation):

    def get_screen(self):
        '''获取屏幕尺寸'''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def left_slide(self):
        logging.info('==========左滑=========')
        size = self.get_screen()
        y1 = int(size[1]*0.5)
        x1 = int(size[0]*0.95)
        x2 = int(size[0]*0.25)
        self.swipe(x1,y1,x2,y1,1000)

    def right_slide(self):
        logging.info('==========右滑==========')
        size = self.get_screen()
        y1 = int(size[1]*0.5)
        x1 = int(size[0]*0.95)
        x2 = int(size[0] * 0.25)
        self.swipe(x2, y1, x1, y1, 1000)

    def up_slide(self):
        logging.info('==========上滑==========')
        size = self.get_screen()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.95)
        y2 = int(size[1] * 0.35)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def down_slide(self):
        logging.info('==========下滑=========')
        size = self.get_screen()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.35)
        y2 = int(size[1] * 0.85)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def get_time(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_img(self, module):
        '''截图保存'''
        time = self.get_time()
        #image_file = os.path.dirname(os.path.dirname(__file__)) + '/results/img/%s_%s.png' % (module, time)
        image_file = IMG_PATH + '/%s_%s.png' % (module, time)
        logging.info('==========截图模块 %s========== ' % module)
        print(image_file)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        '''
        logging.info('==========获取csv文件数据==========')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    print(row)
                    return row



if __name__ == '__main__':
    driver = appium_desired()
    #c = Common(driver)
    #c = Common(driver)
    #c.get_yaml_data()
