#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pytest
from common.logger import Log

@pytest.fixture(scope='function',autouse=True)
def logRecord():
    log = Log()
    log.info('-----开始执行用例-----')
    yield
    log.info('-----用例执行结束-----')


