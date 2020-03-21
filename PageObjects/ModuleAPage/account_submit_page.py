"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 下午 4:39
"""
'''A端提交已选择账号页面行为'''
from PageLocators.ModuleALoc.account_submit_pageloc import Account_submitPage as loc
from Commons.basepage import BasePage


class AccountSubmitPage(BasePage):
    def all_check(self):
        self.click_element(loc.check_all, "提交已选择账号页面_全选账号")

    def order_account_button(self):
        self.click_element(loc.order_msg_button, "提交已选择账号页面_批量添加订单信息")

    def prompt_msg_button(self):
        self.click_element(loc.prompt_msg, "提交已选择账号页面_批量添加订单信息确认按钮")

    def forms_trade_straight(self):
        self.click_element(loc.prompt_msg, "添加订单信息并提交弹框中_合作形式/直发")

    def switch_form(self):
        ele = self.get_element(loc.requirement_description, "切换iframe_需求描述表单")
        self.switch_to_iframe(ele, "添加订单信息并提交弹框中_需求描述")

    def requirement_description_form(self, description):
        self.click_element(loc.shielding, "iframe_需求描述表单_定位到防屏蔽")
        self.input_text(loc.shielding, description, "添加订单信息并提交弹框中_输入需求描述")

    def back_form_iframe(self):
        self.back_iframe("返回主iframe")

    def save_submit_button(self):
        self.click_element(loc.save_button, "添加订单信息并提交弹框中_保存并提交按钮")

    def save_confirm_button(self):
        self.click_element(loc.confirm_button, "添加订单信息并提交弹框中_二次确认按钮")

    def view_button(self):
        self.click_element(loc.view_button, "提交已选择账号页面中_查看已提交活动按钮")
