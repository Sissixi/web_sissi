"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/16 0016 下午 4:53
"""
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.home_b_pageloc import HomeBLoc as loc
'''B端——首页行为'''
class Home_B_Page(BasePage):
    def marked_words_exist(self):
        return self.check_ele_visiable(loc.welcome_msg,"B端首页_微博易内部平台提示语是否存在")
    def mouse_check_loc(self):
        #先调用鼠标悬浮操作
        self.mouse_action(loc.check_loc,"B端首页_鼠标悬浮在审核元素")
    def click_Reservation_check(self):
        self.click_element(loc.Reservation_check,"B端首页_点击审核预约需求审核")

    def mouse_booking_list(self):
        #先调用鼠标悬浮操作
        self.mouse_action(loc.V_M,"B端首页_鼠标悬浮在V代言M元素")

    def click_Booking_list(self):
        self.click_element(loc.Booking_list,"B端首页_点击V代言M下的预约订单列表（M）")