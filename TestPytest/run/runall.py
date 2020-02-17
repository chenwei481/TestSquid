#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pytest
import time


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    file_name = now+'report.html'
    pytest.main(["../testcase/","--html=../results/reports/%s"%file_name,
                 "--junitxml=../results/xml/%s.xml"%file_name])


