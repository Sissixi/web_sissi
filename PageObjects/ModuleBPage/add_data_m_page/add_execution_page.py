"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 3:14
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.add_data_m_loc.add_execution_results_pageloc import Add_execution_resultsLoc as loc

'''
B端-V代言M-预约订单列表 （媒介）-添加执行结果弹框
'''


class Add_execution_page(BasePage):
    def click_all_selecet(self):
        self.click_element(loc.all_selecet, "添加执行结果弹框_全选")

    def send_perform_link(self, text):
        self.input_text(loc.perform_link, text, "添加执行结果弹框_添加执行链接")

    def click_pictures_button(self):
        self.click_element(loc.upload_pictures, "添加执行结果弹框_点击上传按钮")

    def click_upload_pictures(self,filepath):
        self.upload_file(filepath)

    def click_batch_submit(self):
        self.click_element(loc.batch_submit, "添加执行结果弹框_批量提交")

    def click_confirm_button(self):
        self.click_element(loc.confirm_button, "添加执行结果弹框_确定按钮")

    def success_msg_text(self):
        return self.get_text(loc.success_msg, "添加执行结果_成功提示")
