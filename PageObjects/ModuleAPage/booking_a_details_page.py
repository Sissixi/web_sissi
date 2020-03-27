# coding:utf-8
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.booking_a_details_pageloc import Booking_detail_PageLoc as loc

'''
A端-预约订单详情-页面行为
'''


class Booking_a_Page(BasePage):
    def click_confirm_button(self):
        self.click_element(loc.confirm_button, "A端预约订单详情_确认使用功能")

    def click_choose_offer(self):
        self.click_element(loc.choose_offer, "A端预约订单详情_选择报价")

    def click_bounced_confirm_button(self):
        self.click_element(loc.bounced_confirm_button, "A端预约订单详情_确定选择的报价")
    def click_add_execution_content(self):
        self.click_element(loc.add_execution_content,"A端预约订单详情_添加执行内容按钮")
    def click_straight_content(self):
        self.click_element(loc.straight_content,"A端预约订单详情_直发内容添加")
        
