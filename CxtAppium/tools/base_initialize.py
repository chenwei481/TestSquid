#Author:chen
#!/usr/bin/env python
#-*-coding:gb2312-*-
from selenium.webdriver.common.by import By
import logging
from selenium.common.exceptions import NoSuchElementException
from tools.common import Common
from tools.desired_caps import appium_desired
import time
from selenium.webdriver.support.ui import WebDriverWait


class Initialize(Common):
    '''安装APP之后进行的初始化操作'''

    skipBtn = (By.ID, 'com.caixuetang.app:id/skip')  # 跳过启动页
    agreeBtn = (By.ID, 'com.caixuetang.app:id/agree_tv')  # 同意协议
    notagreeBtn = (By.ID, 'com.caixuetang.app:id/not_agree_tv')  # 不同意协议

    def cheak_qidongye(self):
        '''跳过启动页之后滑动4次'''
        logging.info('==========检测启动页=========')
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.error('==========没有检测到启动页=========')
        else:
            logging.info('=========点击跳过启动页=========')
            element.click()
            logging.info("=========滑动4次，进入页面==========")
            for i in range(0, 4):
                time.sleep(1)  # 滑动前等待，不然要报错
                self.left_slide()


    def cheak_agree(self):
        '''安装APP之后点击同意协议'''

        logging.info('==========点击同意协议==========')
        try:
            element = self.driver.find_element(*self.agreeBtn)
        except NoSuchElementException:
            logging.error('=========没有检测到同意协议==========')
        else:
            logging.info('==========进入首页==========')
            element.click()
            self.get_img('首页')


    myBtn = (By.XPATH, '//android.widget.TextView[@text="我的"]')
    denglBtn = (By.XPATH, '//android.widget.TextView[@text="您还没有登录，请先登录"]')
    phoneEdit = (By.ID, 'com.caixuetang.app:id/login_user_name')
    passwordEdit = (By.ID, 'com.caixuetang.app:id/login_user_password')
    loginBtn = (By.ID, 'com.caixuetang.app:id/login_button')

    def login_at(self):
        '''进行登录'''
        try:
            my_element = self.driver.find_element(*self.myBtn)
        except:
            logging.error('===========定位‘我的’失败===========')
        else:
            logging.info('==========点击‘我的’=========')
            my_element.click()

            try:
                #dengl_element = self.driver.find_element(*self.denglBtn)
                dengl_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.denglBtn))
            except:
                logging.error('===========定位‘跳转登录’==============')
            else:
                logging.info('==============点击跳转登录==============')
                time.sleep(3)
                dengl_element.click()
                try:
                    time.sleep(2)
                    phone_element = self.driver.find_element(*self.phoneEdit)
                    pword_element = self.driver.find_element(*self.passwordEdit)
                    login_element = self.driver.find_element(*self.loginBtn)
                except:
                    logging.error('============定位手机号、密码输入框失败==========')
                else:
                    logging.info('=============输入手机号密码，点击登录===========')
                    phone_element.send_keys('17039176000')
                    pword_element.send_keys('123456')
                    login_element.click()

    def main(self,login = None):
        self.cheak_qidongye()
        self.cheak_agree()
        if login == 'run':
            self.login_at()
        else:
            logging.info('=============暂不执行登录===========')




if __name__ == '__main__':
    driver = appium_desired()
    c = Initialize(driver)
    c.cheak_qidongye()
    c.cheak_agree()
    c.login_at()
