#Author：chen
# coding=utf-8
import MySQLdb
import json
import  MySQLdb.cursors

class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='234578xywmun',
            db='pytestapi',
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def carry_out(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        #result = json.dumps(result)
        return result

if __name__ =='__main__':
    op_mysql = OperationMysql()
    res = op_mysql.carry_out("select * from django_migrations WHERE id = 2")
    print(res)