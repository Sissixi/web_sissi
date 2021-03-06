"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/27 0027 下午 10:38
"""
import pytest
from TestDatas.Commons_datas import base_b_url
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page
from PageObjects.ModuleBPage.Check_booking_b_page.order_b_check_search_page import Order_b_check_Page
from PageObjects.ModuleBPage.Check_booking_b_page.booking_requirements_audit_details_page import Review_detailsPage
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from time import sleep

'''B端订单执行内容审核'''


@pytest.fixture
def b_process_review(init):
    init.get(base_b_url)
    # 实例化B端登录行为
    LBP = LoginBPage(init)
    # 实例化B端首页行为
    HBP = Home_B_Page(init)
    yield init, LBP, HBP


@pytest.mark.usefixtures("b_process_review")
class Test_B_content_check:
    @pytest.mark.process
    def test_B_check_reservation(self, b_process_review):
        '''B端预约需求审核'''
        # 调用B端登录行为
        b_process_review[1].loginB(success_b_data["username"], success_b_data["password"])
        # 调用鼠标悬浮到审核操作
        b_process_review[2].mouse_check_loc()
        sleep(1)
        # 点击预约需求审核
        b_process_review[2].click_Reservation_check()
        # 预约审核页面-输入预约需求名称
        Order_b_check_Page(b_process_review[0]).input_requirement_name(BookingData().booking_name)
        # 预约审核页面-查询输入预约需求名称
        Order_b_check_Page(b_process_review[0]).order_click_button()
        sleep(1)
        # 预约审核页面-点击查询到的预约需求名称
        Order_b_check_Page(b_process_review[0]).click_requirement_name()
        sleep(2)
        # 切换到最新窗口
        Order_b_check_Page(b_process_review[0]).switch_new_windows()
        sleep(1)

        # 使用js_操作到底部
        Review_detailsPage(b_process_review[0]).click_handle_js()
        sleep(1)
        # 操作预约订单列表审核通过
        Review_detailsPage(b_process_review[0]).click_auide_all()
        sleep(1)
        Review_detailsPage(b_process_review[0]).click_batch_auide_pass()
        Review_detailsPage(b_process_review[0]).confirm_pop_up()
        Review_detailsPage(b_process_review[0]).confirm_pop_up()
        sleep(2)
        Review_detailsPage(b_process_review[0]).execute_state_is_check()
        # assert Review_detailsPage(b_process_review[0]).execute_state_is_check()


if __name__ == '__main__':
    pytest.main()
