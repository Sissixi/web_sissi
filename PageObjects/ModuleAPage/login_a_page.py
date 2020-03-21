"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 10:12
"""
'''A端登录的页面行为'''
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.login_a_pageloc import Logina as loc


class Logina(BasePage):
    # 登录行为
    def login_form(self, username, password, code):
        self.input_text(loc.login_use, username, "A端登录页面_用户名输入")
        self.input_text(loc.login_pwd, password, "A端登录页面_密码输入")
        self.input_text(loc.login_code, code, "A端登录页面_验证码输入")
        self.click_element(loc.login_button, "A端登录页面_点击提交")

    def login_fail_confirm(self):
        self.operation_popout_confirm("A端登录页面_登录失败点击弹框中确认按钮")

    def login_fail_msg(self):
        return self.operation_popout_text("A端登录页面_登录失败获取失败弹框文本")

    def login_code_none_msg(self):
        return self.get_text(loc.msg_code_null, "A端登录页面_验证码为空登录失败提示信息")
