"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 6:55
"""
import pymysql
from Commons.handle_yaml import do_yaml


class HandleMysql:
    def __init__(self):
        # 建立连接
        self.con = pymysql.connect(host=do_yaml.read_yaml('mysql', 'host'),
                                   user=do_yaml.read_yaml('mysql', 'user'),
                                   password=do_yaml.read_yaml('mysql', 'password'),
                                   database=do_yaml.read_yaml('mysql', 'database'),
                                   port=do_yaml.read_yaml('mysql', 'port'),
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
        # 建立游标对象
        self.cur = self.con.cursor()

    def run(self, sql, args=None, is_more=False):
        # 通过游标对象执行sql
        self.cur.execute(sql, args)
        # 通过连接对象提交
        self.con.commit()
        if is_more:
            # 如果is_more等于False，返回多个
            return self.cur.fetchall()
        else:
            # 如果is_more等于True，返回一个
            return self.cur.fetchone()

    def close(self):
        # 关闭游标对象
        self.cur.close()
        # 关闭连接对象
        self.con.close()


if __name__ == '__main__':
    # 实例化sql对象
    do_mysql = HandleMysql()
    # 执行待添加数据截图sql语句
    sql = 'UPDATE selfmedia_execution_backfill_result SET created_at = date_sub(now(),INTERVAL 3 DAY) WHERE reservation_order_id IN (%s);'
    # 获取待添加数据截图的订单id
    sql2 = 'SELECT * FROM  selfmedia_execution_backfill_result ORDER BY reservation_order_id DESC LIMIT 0,1;'

    data = do_mysql.run(sql2)
    order_id = data["reservation_order_id"]
    # 执行待添加数据截图sql语句
    do_mysql.run(sql, args=order_id)
    # 关闭数据库连接
    do_mysql.close()
