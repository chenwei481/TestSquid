#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tools.base_initialize import Initialize
from tools.desired_caps import appium_desired
import pytest
from hamcrest import *
import logging
from selenium.webdriver.support.ui import WebDriverWait
from tools.common import Common
import time


vipBtn = '//android.widget.TextView[@text="会员中心"]'

exchBtn = '//android.widget.TextView[@text="兑换码"]'

zhkeBtn = '//android.widget.TextView[@text="找课"]'
kecBtn = '//android.widget.TextView[@text="今天测试"]'
xufeiBtn = '//android.widget.TextView[@text="立即续费"]'
wenanBtn = '//android.widget.TextView[@text="千部会员课程战法免费学"]'


#@pytest.mark.skip()
def test_vip():
    driver = appium_desired()
    init = Initialize(driver)
    init.main(login='run')
    vipElement = driver.find_element_by_xpath(vipBtn)
    vipElement.click()
    pr=driver.find_element_by_id("com.caixuetang.app:id/view_top_bar_button_right")
    assert_that(pr.get_attribute('text'), equal_to('记录'))


#@pytest.mark.exch
@pytest.mark.skip()
def test_exchange():
    driver = appium_desired()
    init = Initialize(driver)
    init.main(login='run')
    time.sleep(3)

    #由于结构原因在此自定义滑动比例
    windows = driver.get_window_size()
    x = windows['width'];y = windows['height']
    x1 = int(x * 0.5);y1 = int(y * 0.8);y2 = int(y * 0.3)
    driver.swipe(x1, y1, x1, y2, 1000)
    exch = driver.find_element_by_xpath(exchBtn)
    assert exch.text == '兑换码'

@pytest.mark.skip()
def test_pay():
    driver = appium_desired()
    init = Initialize(driver)
    init.main(login='run')
    try:
        zhkeElement = WebDriverWait(driver,5).until(lambda x: x.find_element_by_xpath(zhkeBtn))
        zhkeElement.click()
    except:
        logging.info('==============定位“找课”失败===============')

    kecElement = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(kecBtn))
    kecElement.click()
    xufeiElement = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(xufeiBtn))
    xufeiElement.click()
    wen = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(wenanBtn))
    assert wen.text == '千部会员课程战法免费学'




