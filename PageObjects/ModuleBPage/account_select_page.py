"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 下午 2:14
"""
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.account_select_pageloc import Select_Account as loc

'''A端选择账号页面行为'''


class AccountSelectPage(BasePage):
    def account_input_name(self, account_name):
        self.input_text(loc.account_input, account_name, "A端选择账号页面_输入账号名称")

    def account_seach_button(self):
        self.click_element(loc.account_button, "A端选择账号页面_搜账号按钮")

    def checkbox_button(self):
        self.click_element(loc.account_select, "A端选择账号页面_选择搜到的账号按钮")

    def view_submit(self):
        self.click_element(loc.View_submit, "A端选择账号页面_查看并提交按钮")
