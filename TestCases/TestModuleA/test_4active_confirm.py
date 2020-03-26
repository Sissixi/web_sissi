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
from PageObjects.ModuleAPage.activity_managePage import ActiveManagePage
from TestDatas.Commons_datas import base_a_url
from TestDatas.ModuleADatas.login_a_datas import success_a_data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
@pytest.fixture
def a_confirm():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_a_url)
    #调用登录行为
    Logina(driver).login_form(success_a_data["username"],success_a_data["password"],success_a_data["code"])
    #实例化活动管理页面行为
    amp=ActiveManagePage(driver)
    yield driver,amp
    driver.quit()
class Test_a_active_confirm:
    def test_active_confirm_process(self,a_confirm):
        #点击首页——活动管理
        HomePage(a_confirm[0]).click_active_manage()
        #点击活动管理页面的预约活动
        a_confirm[1].click_booking_active_button()
        #查询输入框输入预约活动名字
        a_confirm[1].input_booking_name(BookingData().booking_name)
        #点击查询按钮
        a_confirm[1].click_select_button()
        #点击活动详情按钮
        a_confirm[1].click_order_detail()
        #调用新窗口行为
        a_confirm[1].new_window()
        sleep(1)