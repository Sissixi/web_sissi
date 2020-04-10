"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/31 0031 下午 9:40
"""
from Commons.basepage import BasePage
from PageLocators.ModuleNBLoc.home_nb_pageloc import HomeNbLoc as loc

'''
NB端首页--页面行为
'''


class HomeNbPage(BasePage):
    def nb_exist(self):
        return self.check_ele_visiable(loc.nb, "nb端首页_NB是否存在")

    def click_folding_layer(self):
        self.click_element(loc.Folding_layer, "nb首页_点击左下角折叠按钮")

    def click_close_layer(self):
        self.click_element(loc.close_layer, "nb首页_关闭左下角折叠按钮")

    def click_quality_manage(self):
        self.click_element(loc.quality_manage, "nb首页_点击质检管理")

    def click_booking_quality_manage(self):
        self.click_element(loc.booking_quality_manage, "nb首页_点击nb首页_点击质检管理")
