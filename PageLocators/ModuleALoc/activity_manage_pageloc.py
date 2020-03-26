"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/26 0026 下午 6:49
"""
from selenium.webdriver.common.by import By

'''A端活动管理'''


class Activity_ManageLoc:
    # A端活动管理--预约活动按钮
    booking_activities_button = (By.XPATH, '//a[@data-track-prop-source="预约活动"]')
    # 活动名称查询输入框
    active_input = (By.XPATH, '//input[@placeholder="活动名称查询"]')
    # 查询按钮
    select_button = (By.ID, "submitButton")
    # 查看订单详情按钮
    View_order_details = (By.XPATH, '//a[contains(text(),"查看订单详情")]')
