"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 10:06
"""
from selenium.webdriver.common.by import By

'''
A端登录页面元素定位类
'''


class Logina:
    # A端用户名登录
    login_use = (By.ID, "username")
    # A端密码登录
    login_pwd = (By.ID, "password")
    # A端验证码登录
    login_code = (By.ID, 'piccode')
    # A端登录按钮
    login_button = (By.CLASS_NAME, 'btn_wrap')
    #验证码为空提示
    msg_code_null=(By.XPATH,'//p[@class="error picCodeError"]')
