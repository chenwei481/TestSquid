#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pytest
from testview.test_one_view import TestOne
from common.op_data import OperationData
from common.op_excel import OperationExcel

to = TestOne()
od = OperationData()
od.op_data('test1')  #需要预期结果
oe = OperationExcel('test1',0)

def test_one_1():
    result = to.testLogistics()
    exile = od.exile[0]
    oe.write_value(1,8,result)
    assert exile in result

#@pytest.mark.skip()
def test_one_2():
    res = to.testLongude()
    exile = od.exile[1]
    oe.write_value(2,8,res)
    assert exile in res

if __name__ == '__main__':
    pytest.main()