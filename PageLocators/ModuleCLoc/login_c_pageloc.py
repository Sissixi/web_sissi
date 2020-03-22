"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/22 0022 下午 6:51
"""
from selenium.webdriver.common.by import By

'''
C端登录页面
'''


class LoginCLoc:
    username = (By.ID, "login_username")
    password = (By.ID, "login_password")
    Sliding_box = (By.XPATH, '//span[@data-nc-lang="_startTEXT"]')
    button_login = (By.XPATH, '//button[@type="submit"]')
