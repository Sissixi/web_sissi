# coding:utf-8
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.Confirm_to_use_loc.booking_a_details_pageloc import Booking_detail_PageLoc as loc

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
        self.click_element(loc.add_execution_content, "A端预约订单详情_添加执行内容按钮")

    def click_straight_content(self):
        self.click_element(loc.straight_content, "A端预约订单详情_点击直发内容输入框")

    def js_input(self, text):
        self.js_value(loc.attr_value, text, "A端预约订单详情_输入直发内容输入框内容")

    def loc_select_live_video(self, textvalue):
        self.select_value(loc.select_live_video, textvalue, "A端预约订单详情_选择是否含有视频/直播")

    def start_time(self, timevalue):
        self.js_time(loc.execute_start_time, timevalue, "A端预约订单详情_执行开始时间")

    def end_time(self, endtimevalue):
        self.js_time(loc.execute_end_time, endtimevalue, "A端预约订单详情_执行结束时间")

    def click_submit_content(self):
        self.click_element(loc.submit_content, "A端预约订单详情_提交执行内容")

    def click_confirm_commit(self):
        self.click_element(loc.confirm_commit, "A端预约订单详情_确认提交按钮")

    def click_msg_success(self):
        return self.get_text(loc.msg_success, "A端预约订单详情_提交执行内容成功提示信息")
