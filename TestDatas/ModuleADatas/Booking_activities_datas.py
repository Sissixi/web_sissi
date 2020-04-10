"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 下午 12:58
"""
'''A端预约活动页面用到的数据'''
import datetime
import time


class BookingData:
    '''填写预约需求页面数据'''
    # 填写预约需求名字
    # booking_name = "webzdh"
    booking_name = "webzdh" + time.strftime("%Y-%m-%d")
    # 填写预约需求描述
    description_content = "wbzdh测试"
    # 填写预约需求--选择预计推广开始时间
    start_time = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime("%Y-%m-%d %H:%M")
    # 填写预约需求--选择预计推广结束时间
    end_time = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d %H:%M")
    # 填写预约需求--选择预约结果反馈时间
    feedback_time = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M")
    '''选择账号页面数据'''
    #账号名字
    account_name = "我是娜扎"
    '''提交已选择账号页面'''
    # 需求描述内容
    content_msg = "测试数据"
