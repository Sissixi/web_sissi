"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/28 0028 上午 10:58
"""
from Commons.basepage import BasePage
from PageLocators.ModuleALoc.Confirm_to_use_loc.booking_list_pageloc import Booking_listLoc as loc

'''
A端活动管理-预约活动页面详情
'''


class BookingListPage(BasePage):
    def is_exist_loc(self):
        return self.check_ele_visiable(loc.active_state, "A端预约活动详情_预约状态是否存在")
