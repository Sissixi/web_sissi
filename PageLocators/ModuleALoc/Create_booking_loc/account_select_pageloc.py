"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 下午 1:57
"""
from selenium.webdriver.common.by import By
'''A端预约活动选择账号页面'''
class Select_Account:
    #选择微博账号输入框元素定位
    account_input=(By.XPATH,'//input[@class="search_input"]')
    #搜微博账号按钮
    account_button=(By.XPATH,'//a[@class="search_button"]')
    #选择账号
    account_select=(By.XPATH,'//tr[@account_id="6600418"]//input[@name="account_id"]')
    #查看并提交按钮
    View_submit=(By.XPATH,'//span[text()="查看并提交已选账号"]')
