"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/23 0023 下午 8:57
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.booking_list_MLoc import Booking_listLoc as loc

'''
B端-V代言M-预约订单列表 （媒介）-待应约页面行为
'''


class Booking_listM_Page(BasePage):
    def input_requirement_name(self, name):
        self.input_text(loc.requirement_name, name, "预约订单列表（媒介）_输入需求名称进行搜索")

    def click_Query_button(self):
        self.click_element(loc.Query_button, "预约订单列表（媒介）_查询")

    def click_accept_button(self):
        self.click_element(loc.accept_button, "预约订单列表（媒介）_应约按钮")
