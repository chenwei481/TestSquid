#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from momo_testProject.comm.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('==========setUp==========')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('==========tearDown==========')
        sleep(5)
        self.driver.close_app()