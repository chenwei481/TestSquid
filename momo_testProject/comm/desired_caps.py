#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config
import os

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():

    #读取yaml文件
    with open('../config/desired_caps.yaml','r',encoding='utf-8') as file:
        data = yaml.load(file,Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] =data['platformName']

    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    base_path = os.path.dirname(os.path.dirname(__file__))  # 获取到当前文件的路径
    app_path = os.path.join(base_path, 'app', data['app'])  #获取app的路径做拼接
    desired_caps['app'] = app_path

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']

    desired_caps['noReset']=data['noReset']   #保持之前的元素状态（开启中文配置，此项必须开启）

    #输入中文时，需要的配置
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    #需要定位toast必须要这个参数
    desired_caps['automationName']= data['automationName']

    logging.info('启动app')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)  #等待页面元素的加载,隐式等待
    return driver


if __name__ == '__main__':
    appium_desired()

    #with open('../config/desired_caps.yaml','r',encoding='utf-8') as file:
     #   data = yaml.load(file,Loader=yaml.FullLoader)
    #base_path = os.path.dirname(os.path.dirname(__file__))   #获取到当前文件的路径
    #app_path = os.path.join(base_path, 'app', data['app'])
    #print(base_path)
    #print(app_path)