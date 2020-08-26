#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pytest
import logging

@pytest.fixture(scope='function',autouse=True)
def logRecord():

    logging.info('-----开始执行用例-----')

    yield
    logging.info('-----用例执行结束-----')


