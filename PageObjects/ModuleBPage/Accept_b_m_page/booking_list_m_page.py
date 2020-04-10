"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/23 0023 下午 8:57
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.Accept_b_m_loc.booking_list_m_pageLoc import Booking_listLoc as loc

'''
B端-V代言M-预约订单列表 （媒介）-页面行为
'''


class Booking_listM_Page(BasePage):
    def input_requirement_name(self, name):
        self.input_text(loc.requirement_name, name, "预约订单列表（媒介）_输入需求名称进行搜索")

    def click_Query_button(self):
        self.click_element(loc.Query_button, "预约订单列表（媒介）_查询")

    def click_accept_button(self):
        self.click_element(loc.accept_button, "预约订单列表（媒介）_应约按钮")

    def success_msg(self):
        return self.get_text(loc.accept_success_msg, "应约成功_提示信息")

    def js_scroll_all_order(self):
        self.js_bottom("预约订单列表（媒介）_操作滚动条到全部订单可见")

    def click_all_order(self):
        self.click_element(loc.all_order, "预约订单媒介_点击全部订单tab")

    def click_add_result(self):
        self.click_element(loc.add_result, "预约订单媒介_点击添加执行结果")

    def click_add_screenshot(self):
        self.click_element(loc.add_screenshot, "预约订单媒介_点击添加/修改数据截图")
