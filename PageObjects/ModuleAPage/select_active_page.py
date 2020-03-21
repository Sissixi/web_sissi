"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/21 0021 下午 11:20
"""
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.select_active_pageloc import SelectPage as loc

'''A端选择投放平台页面封装'''


class SelectPlat(BasePage):
    def click_sina(self):
        self.click_element(loc.select_weibo_platform, "A端创建活动页面_点击新浪平台")
        self.click_element(loc.weibo_yuyue, "A端创建活动页面_点击新浪预约活动")
