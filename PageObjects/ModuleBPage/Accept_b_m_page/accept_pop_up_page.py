"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/23 0023 下午 8:55
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.Accept_b_m_loc.accept_pop_up_pageloc import accept_popLoc as loc

'''
B端预约订单列表媒介-应约弹框-应约回复/价格信息页面行为
'''


class Accept_pop_page(BasePage):
    def select_top_link(self, text_content):
        self.select_value(loc.top_link, text_content, "应约弹框_应约备注_带要求的话题/@/链接")

    def click_accept_button(self):
        self.click_element(loc.accept_button, "应约弹框_点击应约按钮")

    def click_js_iframe(self, text):
        self.js_iframe(loc.iframe_id, text, "通过js切换到iframe中_body中输入应约回复")

    def click_button(self):
        self.click_element(loc.button, "应约弹框_提交按钮")

    def click_confirm_button(self):
        self.click_element(loc.confirm_button, "应约弹框_二次确认按钮")
