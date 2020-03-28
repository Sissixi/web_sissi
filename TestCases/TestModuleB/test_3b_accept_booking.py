"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/23 0023 下午 9:36
"""
import pytest
from TestDatas.Commons_datas import base_b_url
from time import sleep
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page
from PageObjects.ModuleBPage.Accept_b_m_page.booking_list_m_page import Booking_listM_Page
from PageObjects.ModuleBPage.Accept_b_m_page.accept_pop_up_page import Accept_pop_page
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from TestDatas.ModuleBDatas.order_b_datas import B_Data

'''
B端媒介应约
'''


@pytest.fixture
def b_accept_process(init):
    '''前置'''
    init.get(base_b_url)
    # 实例化B端登录行为
    LBP = LoginBPage(init)
    # 实例化B端首页行为
    HBP = Home_B_Page(init)
    # 实例化B端预约订单列表（媒介端）行为操作
    BLP = Booking_listM_Page(init)
    # 实例化B端弹框页面行为
    ap = Accept_pop_page(init)
    yield init, LBP, HBP, BLP, ap
    '''后置'''
    init.quit()


@pytest.mark.usefixtures("b_accept_process")
class Test_Accept_process:
    def test_b_accept_process(self, b_accept_process):
        '''B端应约'''
        # 调用B端登录行为
        b_accept_process[1].loginB(success_b_data["username"], success_b_data["password"])
        # B端首页_鼠标悬浮在V代言M元素
        b_accept_process[2].mouse_booking_list()
        sleep(1)
        # 点击V_代言M——预约订单列表
        b_accept_process[2].click_Booking_list()
        # 预约订单列表（媒介）-输入需求名称
        b_accept_process[3].input_requirement_name(BookingData.booking_name)
        # 预约订单列表（媒介）-查询
        b_accept_process[3].click_Query_button()
        sleep(1)
        # 预约订单列表（媒介）-应约
        b_accept_process[3].click_accept_button()
        sleep(1)
        # 应约弹框_应约备注
        b_accept_process[4].select_top_link(B_Data.value_text)
        sleep(1)
        # 应约弹框_应约按钮
        b_accept_process[4].click_accept_button()
        sleep(1)
        # 应约弹框_输入应约回复
        b_accept_process[4].click_js_iframe(B_Data.replace_content)
        sleep(1)
        # 应约弹框_提交按钮
        b_accept_process[4].click_button()
        sleep(1)
        # 应约弹框_提交后确认按钮
        b_accept_process[4].click_confirm_button()
        sleep(1)
        assert b_accept_process[3].success_msg() == B_Data.success_msg


if __name__ == '__main__':
    pytest.main()
