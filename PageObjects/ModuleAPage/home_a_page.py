"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/21 0021 下午 8:55
"""
from PageLocators.ModuleALoc.home_a_pageloc import HomeLoc as loc
from Commons.basepage import BasePage

'''A端首页'''


class HomePage(BasePage):
    # 点击首页创建活动按钮行为
    def click_creat_button(self):
        self.click_element(loc.create_buttom, "A端首页_点击创建活动")

    # 创建按钮是否存在
    def button_is_exist(self):
        '''如果创建活动按钮存在就返回True,否则返回False'''
        return self.check_ele_visiable(loc.create_buttom, "A端首页_创建活动按钮元素存在就返回True")
    #切换到最新窗口句柄
    def new_current(self):
        self.switch_to_new_window()

    #点击活动管理
    def click_active_manage(self):
        self.click_element(loc.activity_manage,"A端首页_点击活动管理按钮")

