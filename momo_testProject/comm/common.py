#Author:chen
#!/usr/bin/env python
#-*-coding:gb2312-*-
from momo_testProject.baseLocation.baseLocation import BaseLocation
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from momo_testProject.comm.desired_caps import appium_desired
import time
import os
import csv

class Common(BaseLocation):
    #是否同意协议按钮
    adressBtn=(By.ID,'com.immomo.momo:id/confirm_tv')
    cancelBtn=(By.ID,'com.immomo.momo:id/cancel_tv')

    #进入到登录界面按钮
    registerBtn=(By.ID,'com.immomo.momo:id/btn_register')
    loginBtn=(By.ID,'com.immomo.momo: id / tv_account_login')


    phoneBtn=(By.ID,'com.immomo.momo:id/login_et_momoid')
    cipherBtn=(By.ID,'com.immomo.momo:id/login_et_pwd')
    okBtn=(By.ID,'com.immomo.momo:id/btn_ok')

    def cheak_adress(self):
        logging.info('==========检测是否同意协议=========')

        try:
            element = self.driver.find_element(*self.adressBtn)
        except NoSuchElementException:
            logging.info('==========没有检测到同意协议按钮=========')
        else:
            logging.info('=========同意协议=========')
            element.click()

    def login_ui(self):
        logging.info('==========进入登录界面==========')
        self.driver.implicitly_wait(8)
        try:
            element = self.driver.find_element(*self.registerBtn)
        except NoSuchElementException:
            logging.info('=========没有检测到注册登录按钮==========')
        else:
            logging.info('==========进入注册登录界面==========')
            element.click()

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
        driver.swipe(x1, y1, x1, y2, 1000)

    def down_slide(self):
        logging.info('==========下滑=========')
        size = self.get_screen()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.35)
        y2 = int(size[1] * 0.85)
        driver.swipe(x1, y1, x1, y2, 1000)

    def get_time(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_img(self, module):
        '''截图保存'''
        time = self.get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/results/img/%s_%s.png' % (module, time)

        logging.info('==========截图模块 %s========== ' % module)
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
    c = Common(driver)
    c.cheak_adress()
    c.login_ui()
    c.get_img('login')
    c.get_csv_data('../data/data1.csv',1)