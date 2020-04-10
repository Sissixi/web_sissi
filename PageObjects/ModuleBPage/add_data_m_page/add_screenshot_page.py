"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 10:02
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.add_data_m_loc.add_screenshot_pageloc import ADD_screenshotLoc as loc

''''
B端-V代言M-预约订单列表 （媒介）-添加数据截图弹框
'''


class Add_screenshotpage(BasePage):
    def click_all_select(self):
        self.click_element(loc.all_select, "添加数据截图弹框_全选")

    def operate_upload_cilck(self):
        self.click_element(loc.upload_cilck, "添加数据截图弹框_点击上传")

    def send_upload_cilck(self, filepath):
        self.upload_file(filepath)

    def operate_send_people(self, text):
        self.input_text(loc.send_people, text, "添加数据截图弹框_送达人数")

    def operate_batch_submit(self):
        self.click_element(loc.batch_submit, "添加数据截图弹框_批量提交")

    def operate_confirm_button(self):
        self.click_element(loc.confirm_button, "添加数据截图弹框_确认提交")

    def get_text_msg(self):
        return self.get_text(loc.submit_success_msg, "提交成功提示语")
