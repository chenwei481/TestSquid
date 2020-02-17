#Author:chen
#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pytest
from testview.test_two_view import TestTwo
from common.op_data import OperationData
from common.op_excel import OperationExcel

tt = TestTwo()
od = OperationData()
od.op_data('test2')
oe = OperationExcel('test2',0)

def test_two_1():
    res = tt.testTaobao()
    exile = od.exile[0]
    oe.write_value(1,8,res)
    assert exile in res

if __name__ == '__main__':
    pytest.main()
