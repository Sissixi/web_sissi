"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/23 0023 下午 2:11
"""
from selenium.webdriver.common.by import By

'''B端首页页面元素定位'''
class HomeBLoc:

    #微博易内部平台
    welcome_msg=(By.XPATH,'//div[@id="title"]')
    #审核元素定位
    check_loc=(By.XPATH,'//a[text()="审核"]')
    #预约需求审核
    Reservation_check=(By.XPATH,"//a[text()='预约需求审核']")
    #预约需求列表
    Booking_list=(By.XPATH,'//a[text()="预约订单列表（M）"]')

