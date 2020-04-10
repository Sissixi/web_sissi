"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/4/1 0001 上午 10:40
"""
from Commons.basepage import BasePage
from PageLocators.ModuleNBLoc.quality_nb_pageloc import QualityPageLoc as loc

'''
NB端质检页面行为
'''


class QualityNbPage(BasePage):
    def click_link_invalid(self):
        self.click_element(loc.link_invalid, "nb质检页面_选择执行结果不合格原因")

    def input_Deduct_percentage(self, text):
        self.input_text(loc.Deduct_percentage, text, "nb质检页面_输入质检扣款比例")

    def click_submit_button(self):
        self.click_element(loc.submit_button, "nb质检页面_点击提交按钮")

    def click_allow_quality(self):
        self.click_element(loc.allow_quality, "nb质检页面_同意质检结果")

    def click_confirm_allow_quality(self):
        self.click_element(loc.confirm_allow_quality, "nb质检页面_确认同意质检结果")
