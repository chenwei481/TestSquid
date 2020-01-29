#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
class BaseLocation(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        '''元素定位'''
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        '''元素集定位'''
        return self.driver.find_elements(*loc)

    def get_window_size(self,*loc):
        '''获取屏幕尺寸'''
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        '''滑动坐标点'''
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
