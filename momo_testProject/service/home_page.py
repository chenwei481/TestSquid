#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import logging
from momo_testProject.comm.common import Common
from selenium.common.exceptions import NoSuchElementException
from momo_testProject.comm.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class HomePage(Common):
    imageBtn = (By.CLASS_NAME,'android.widget.ImageButton')
    removeBtn = (By.ID,'android:id/button2')
    manBtn = (By.ID,'com.immomo.momo:id/tv_male')
    homeBtn = (By.ID,'com.immomo.momo:id/iv_tab_nearby')

    def get_to_home(self):
        '''进入首页'''
        self.cheak_adress()
        self.login_ui()

        logging.info('==========回到APP首页========')
        try:
            self.driver.implicitly_wait(5)
            element = self.driver.find_element(*self.imageBtn)
        except NoSuchElementException:
            logging.info('==========没有检测到左上角退出按钮==========')
        else:
            logging.info('=========点击退出注册登录界面=========')
            element.click()

            try:
                element_remove = self.driver.find_element(*self.removeBtn)
            except NoSuchElementException:
                logging.info('==========没有检测到取消按钮==========')
            else:
                logging.info('===========点击取消==========')
                element_remove.click()

                try:
                    element_man = self.driver.find_element(*self.manBtn)
                except NoSuchElementException:
                    logging.info('==========没有检测到选择按钮==========')
                else:
                    logging.info('==========点击选择=========')
                    element_man.click()
                    self.driver.implicitly_wait(2)


    def cheak_home(self):
        '''检测是否进入到了首页'''
        self.get_to_home()
        try:
            element = self.driver.find_element(*self.homeBtn)
        except NoSuchElementException:
            logging.info('==========没有检测到首页==========')
            self.get_img('home')
            return False
        else:
            logging.info('==========检测到首页==========')
            return True


if __name__ == '__main__':
    drive = appium_desired()
    h = HomePage(drive)
    h.cheak_home()




