"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 上午 10:36
"""
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.Create_booking_loc.fill_form_pageloc import FillFormPageLoc as loc


class FillPage(BasePage):
    '''填写预约需求页面'''

    def input_name(self, nametext):
        self.input_text(loc.name, nametext, "填写预约需求页面_预约需求名称")

    def input_description(self, conttext):
        self.click_element(loc.description, "填写预约需求页面_切换到iframe")
        self.input_text(loc.description, conttext, "填写预约需求页面_预约需求描述")

    def Execute_start_time(self, timevalue):
        self.js_time(loc.start_time, timevalue, "填写预约需求页面_预计推广开始时间")

    def Execute_end_time(self, timevalue):
        self.js_time(loc.end_time, timevalue, "填写预约需求页面_预计推广结束时间")

    def Execute_feedback_time(self, timevalue):
        self.js_time(loc.feedback_time, timevalue, "填写预约需求页面_预约结果反馈时间")

    def select_trade_button(self):
        self.click_element(loc.select_button, "填写预约需求页面_推广产品所属行业")
        self.click_element(loc.trade_button, "填写预约需求页面_选择美妆日化行业")

    def cilck_next_button(self):
        self.click_element(loc.next_button, "填写预约需求页面_下一步按钮")
