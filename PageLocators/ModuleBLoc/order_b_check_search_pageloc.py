"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/16 0016 下午 6:16
"""
from selenium.webdriver.common.by import By

'''
B端预约-需求审核-搜索页面元素定位
'''
class Order_checkloc:
    # 输入框-需求名称
    requirement_name_input = (By.XPATH, '//input[@name="requirement_name"]')
    # 查询按钮
    order_button = (By.ID, "requirement_search")
    # 点击预约需求名称
    requirement_name_click = (By.LINK_TEXT, "webzdh")
