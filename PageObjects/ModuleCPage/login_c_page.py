"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/22 0022 下午 7:10
"""
from Commons.basepage import BasePage
from PageLocators.ModuleCLoc.login_c_pageloc import LoginCLoc as loc
'''
C端登录页面行为
'''
class LoginCPage(BasePage):
    def loginc(self,username,password):
        self.input_text(loc.username,username,"C端登录页面_输入用户名")
        self.input_text(loc.password,password,"C端登录页面_输入密码")