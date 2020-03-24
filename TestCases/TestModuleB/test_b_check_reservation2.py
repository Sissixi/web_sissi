"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/16 0016 下午 5:57
"""
import pytest
from selenium import webdriver
from TestDatas.Commons_datas import base_b_url
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page
from PageObjects.ModuleBPage.order_b_check_search_page import Order_b_check_Page
from PageObjects.ModuleBPage.Booking_requirements_Audit_details_page import Review_detailsPage
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from time import sleep

'''B端预约需求审核'''


@pytest.fixture
def b_process():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_b_url)
    # 实例化B端登录行为
    LBP = LoginBPage(driver)
    # 实例化B端预约审核行为
    HBP = Home_B_Page(driver)
    yield driver, LBP, HBP
    driver.quit()


@pytest.mark.usefixtures("b_process")
class Test_B_check:
    def test_B_check_reservation(self, b_process):
        '''B端预约需求审核'''
        # 调用B端登录行为
        b_process[1].loginB(success_b_data["username"], success_b_data["password"])
        # 调用鼠标悬浮到审核操作
        b_process[2].mouse_check_loc()
        sleep(1)
        # 点击预约需求审核
        b_process[2].click_Reservation_check()
        # 预约审核页面-输入预约需求名称
        Order_b_check_Page(b_process[0]).input_requirement_name(BookingData().booking_name)
        # 预约审核页面-查询输入预约需求名称
        Order_b_check_Page(b_process[0]).order_click_button()
        # 预约审核页面-点击查询到的预约需求名称
        Order_b_check_Page(b_process[0]).click_requirement_name()
        # 切换到最新窗口
        Order_b_check_Page(b_process[0]).switch_new_windows()
        # 操作预约需求审核通过
        Review_detailsPage(b_process[0]).click_check_comment()
        Review_detailsPage(b_process[0]).confirm_bounced()
        Review_detailsPage(b_process[0]).confirm_pop_up()
        # 操作预约订单列表审核通过
        Review_detailsPage(b_process[0]).click_auide_all()
        Review_detailsPage(b_process[0]).click_batch_auide_pass()
        Review_detailsPage(b_process[0]).confirm_pop_up()


if __name__ == '__main__':
    pytest.main()
