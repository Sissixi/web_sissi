"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/26 0026 下午 7:02
"""
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.Confirm_to_use_loc.activity_manage_pageloc import Activity_ManageLoc as loc

'''
A端活动管理-预约活动页面详情
'''


class ActiveManagePage(BasePage):
    # 点击预约活动tab
    def click_booking_active_button(self):
        self.click_element(loc.booking_activities_button, "A端活动管理_切换预约活动tab")

    def input_booking_name(self, text_name):
        self.input_text(loc.active_input, text_name, "预约活动tab_预约名称输入")

    def click_select_button(self):
        self.click_element(loc.select_button, "预约活动tab_点击查询按钮")

    def click_booking_name(self):
        self.click_element(loc.booking_name, "预约活动tab_点击预约活动名称")

    def click_order_detail(self):
        self.click_element(loc.View_order_details, "预约活动tab_点击查看订单详情")

    def new_window(self):
        # 获取最新窗口页面
        self.switch_to_new_window()
