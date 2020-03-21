"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/23 0023 下午 1:49
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.login_b_pageloc import LoginBLoc as loc

'''B端页面登录行为'''

class LoginBPage(BasePage):
    def loginB(self, username, pawd):
        self.input_text(loc.username, username, "B端登录_用户名输入")
        self.input_text(loc.password, pawd, "B端登录_密码输入")
        self.click_element(loc.button, "B端登录_提交按钮")
