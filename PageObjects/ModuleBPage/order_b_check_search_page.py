"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/16 0016 下午 6:39
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.order_b_check_search_pageloc import Order_checkloc as loc

'''B端预约订单-审核搜索-页面行为'''


class Order_b_check_Page(BasePage):
    def input_requirement_name(self, text):
        self.input_text(loc.requirement_name_input, text, "B端预约订单审核搜索页面_输入需求名称")

    def order_click_button(self):
        self.click_element(loc.order_button, "B端预约订单审核搜索页面_点击查询按钮")

    def click_requirement_name(self):
        self.click_element(loc.requirement_name_click, "B端预约订单审核搜索页面_点击查到的需求名称超链接")
    def switch_new_windows(self):
        #切换至最新窗口
        self.switch_to_new_window()
