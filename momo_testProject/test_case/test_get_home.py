#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
from momo_testProject.comm.unit import StartEnd
from momo_testProject.service.home_page import HomePage
import unittest

class TestHome(StartEnd):

    def test_home(self):
        h = HomePage(self.driver)
        self.assertFalse(h.cheak_home())

if __name__ == '__main__':
    unittest.main()
