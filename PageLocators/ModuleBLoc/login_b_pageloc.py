"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/23 0023 下午 1:45
"""
from selenium.webdriver.common.by import By

'''
B端登录页面元素定位
'''

class LoginBLoc:
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    button = (By.TAG_NAME, 'button')
