"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/31 0031 下午 8:41
"""
import time
import pytest
from Commons.handle_yaml import do_yaml
from Commons.handle_mysql import HandleMysql
from TestDatas.Commons_datas import Quality_script_test

'''
进预约质检执行sql及脚本
'''


class Test_NB_Quality:
    @pytest.mark.process
    def test_nb_quality_test(self, init):
        # 实例化sql
        do_mysql = HandleMysql()
        # 查到selfmedia_execution_backfill_result表中最大id
        max_order_id = do_mysql.run(do_yaml.read_yaml('mysql', 'get_sql_order_id'))
        # 通过字典方法取出最大id
        order_id = max_order_id["reservation_order_id"]
        # 修改预约订单的执行完成时间（执行完成时间前推72小时)
        do_mysql.run(do_yaml.read_yaml('mysql', 'order_completed_time'), args=order_id)
        # 修改预约订单的上传数据数据截图时间（数据截图时间前推6小时）
        do_mysql.run(do_yaml.read_yaml('mysql', 'screenshot_time'), args=order_id)
        # 关闭sql连接
        do_mysql.close()
        # 跑质检脚本
        init.get(Quality_script_test)
        time.sleep(50)

    if __name__ == '__main__':
        pytest.main()
