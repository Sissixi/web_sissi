"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/26 0026 下午 7:29
"""
import pytest

from selenium import webdriver
from time import sleep
from PageObjects.ModuleAPage.home_a_page import HomePage
from PageObjects.ModuleAPage.login_a_page import Logina
from PageObjects.ModuleAPage.Confirm_to_use_page.booking_a_details_page import Booking_a_Page
from PageObjects.ModuleAPage.Confirm_to_use_page.activity_manage_page import ActiveManagePage
from TestDatas.Commons_datas import base_a_url
from TestDatas.ModuleADatas.login_a_datas import success_a_data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from TestDatas.ModuleADatas import booking_detail_datas as bdd

'''A端确认应约使用'''


@pytest.fixture
def a_confirm(init):
    init.get(base_a_url)
    # init.get("http://chuanbo.tst-weiboyi.com/hwreservation/order/detail/id/58631")
    # 调用登录行为
    Logina(init).login_form(success_a_data["username"], success_a_data["password"], success_a_data["code"])
    # 实例化活动管理页面行为
    amp = ActiveManagePage(init)
    # 实例化预约详情页面行为
    bap = Booking_a_Page(init)
    yield init, amp, bap


class Test_a_active_confirm:
    def test_active_confirm_process(self, a_confirm):
        # 点击首页——活动管理
        HomePage(a_confirm[0]).click_active_manage()
        # 点击活动管理页面的预约活动
        a_confirm[1].click_booking_active_button()
        # 查询输入框输入预约活动名字
        a_confirm[1].input_booking_name(BookingData().booking_name)
        # 点击查询按钮
        a_confirm[1].click_select_button()
        # 点击活动详情按钮
        a_confirm[1].click_order_detail()
        # 调用新窗口行为
        a_confirm[1].new_window()
        sleep(1)

        # 预约订单详情页-点击确认使用
        a_confirm[2].click_confirm_button()
        # 预约订单详情页-点击选择报价
        a_confirm[2].click_choose_offer()
        # 预约订单详情页-点击确认报价
        a_confirm[2].click_bounced_confirm_button()
        # 预约订单详情页-点击添加执行内容
        a_confirm[2].click_add_execution_content()
        # 预约订单详情页-点击直发内容输入框
        a_confirm[2].click_straight_content()
        # 预约订单详情页-输入直发内容
        a_confirm[2].js_input(bdd.straight_content)
        # 是否含有视频/直播下拉框操作
        a_confirm[2].loc_select_live_video(bdd.select_live_video)
        # 执行时间操作
        a_confirm[2].start_time(bdd.start_time)
        a_confirm[2].end_time(bdd.end_time)
        sleep(1)
        # 点击提交执行内容
        a_confirm[2].click_submit_content()
        sleep(1)
        # 确认提交
        a_confirm[2].click_confirm_commit()
        sleep(1)
        assert "操作成功" == a_confirm[2].click_msg_success()


if __name__ == '__main__':
    pytest.main()
