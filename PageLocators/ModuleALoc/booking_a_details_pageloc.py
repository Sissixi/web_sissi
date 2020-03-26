"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/26 0026 下午 8:27
"""
from selenium.webdriver.common.by import By
'''
A端-预约订单详情-元素定位
'''
class Booking_detail_PageLoc:
    #确认使用按钮
    confirm_button=(By.ID,"reservationDetail")
    #确认使用_弹框提示中——选择报价
    choose_offer=(By.NAME,"choice_price")
    #确认使用_弹框提示中——确认按钮
    bounced_confirm_button=(By.XPATH,'//a[@class="btn_small_important weiboyiWindow_btn button"]')
    #添加执行内容
    add_execution_content=(By.ID,"addExecutionDocAndExecute")
    #定位到直发内容输入框
    straight_content=(By.XPATH,'//textarea[@class="js_content"]')