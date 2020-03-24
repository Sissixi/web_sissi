"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/23 0023 下午 8:55
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.accept_pop_upLoc import accept_popLoc as loc

'''
B端预约订单列表媒介-应约弹框-应约回复/价格信息页面行为
'''


class Accept_pop_page(BasePage):
    def select_top_link(self, text_content):
        self.select_value(loc.top_link, text_content, "应约弹框_应约备注_带要求的话题/@/链接")

    def click_accept_button(self):
        self.click_element(loc.accept_button, "应约弹框_点击应约按钮")

    def switch_to_reply_box(self):
        ele = self.click_element(loc.accept_reply, "应约弹框_应约回复输入框")
        # 此处传的是WebElement对象,ele=WebElement对象
        self.switch_to_iframe(ele, "切换iframe_应约回复输入框")
    def send_accept_content(self, text):
        self.input_text(loc.accept_content, text, "应约弹框_输入应约回复")

    def back_form_iframe(self):
        self.back_iframe("返回主iframe")

    def click_button(self):
        self.click_element(loc.button, "应约弹框_提交按钮")

    def click_confirm_button(self):
        self.click_element(loc.confirm_button, "应约弹框_二次确认按钮")
