"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 3:32
"""
import pytest
from TestDatas.Commons_datas import base_b_url
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page
from PageObjects.ModuleBPage.Accept_b_m_page.booking_list_m_page import Booking_listM_Page
from PageObjects.ModuleBPage.add_data_m_page.add_execution_page import Add_execution_page
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleBDatas.order_b_datas import B_Data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from time import sleep

'''B端订单添加执行结果'''


@pytest.fixture
def b_add_result(init):
    # 获取地址
    init.get(base_b_url)
    # 实例化B端登录行为
    LBP = LoginBPage(init)
    # 实例化B端首页行为
    HBP = Home_B_Page(init)
    # 实例化B端预约订单列表（媒介端）行为
    BLP = Booking_listM_Page(init)
    # 实例化B断言预约订单列表（媒介端）添加执行结果行为
    AEP = Add_execution_page(init)
    yield init, LBP, HBP, BLP, AEP


class Test_B_add_result:
    @pytest.mark.process
    @pytest.mark.usefixtures('b_add_result')
    def test_b_add_execution_result(self, b_add_result):
        # 调用B端登录行为
        b_add_result[1].loginB(success_b_data["username"], success_b_data["password"])
        # B端首页_鼠标悬浮在V代言M元素
        b_add_result[2].mouse_booking_list()
        sleep(1)
        # 点击V_代言M——预约订单列表
        b_add_result[2].click_Booking_list()
        sleep(3)
        # js滚动条-滚动到全部订单可见
        b_add_result[3].js_scroll_all_order()
        sleep(5)
        # 切换至全部订单
        b_add_result[3].click_all_order()
        # 预约订单列表（媒介）-输入需求名称
        b_add_result[3].input_requirement_name(BookingData.booking_name)
        # 预约订单列表（媒介）-查询
        b_add_result[3].click_Query_button()
        # 添加执行结果
        b_add_result[3].click_add_result()
        sleep(1)
        # 添加执行结果弹框-全选
        b_add_result[4].click_all_selecet()
        # 添加执行结果弹框-输入执行链接
        b_add_result[4].send_perform_link(B_Data.Perform_link)
        # 添加执行结果弹框-点击上传按钮
        b_add_result[4].click_pictures_button()
        sleep(5)
        # 添加执行结果弹框-图片文件上传
        b_add_result[4].click_upload_pictures(B_Data.path)
        sleep(2)
        # 添加执行结果弹框-点击批量提交
        b_add_result[4].click_batch_submit()
        # 添加执行结果弹框-确定按钮
        b_add_result[4].click_confirm_button()
        # 断言
        assert b_add_result[4].success_msg_text() == B_Data.add_executable


if __name__ == '__main__':
    pytest.main()
