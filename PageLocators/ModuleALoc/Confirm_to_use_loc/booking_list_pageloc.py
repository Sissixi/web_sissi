"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/28 0028 上午 10:55
"""
from selenium.webdriver.common.by import By

'''
A端-预约活动-预约活动详情-元素定位
'''
class Booking_listLoc:
    # 预约活动状态
    active_state = (By.XPATH, '//em[@class="color_activation"]')
