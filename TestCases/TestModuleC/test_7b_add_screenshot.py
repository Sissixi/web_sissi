"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 10:14
"""
import pytest
from TestDatas.Commons_datas import base_b_url
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page
from PageObjects.ModuleBPage.Accept_b_m_page.booking_list_m_page import Booking_listM_Page
from PageObjects.ModuleBPage.add_data_m_page.add_screenshot_page import Add_screenshotpage
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleBDatas.order_b_datas import B_Data
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from time import sleep

'''B端预约订单（媒介端）添加数据截图'''


@pytest.fixture
def b_add_screenshot(init):
    # 获取地址
    init.get(base_b_url)
    # 实例化B端登录行为
    LBP = LoginBPage(init)
    # 实例化B端首页行为
    HBP = Home_B_Page(init)
    # 实例化B端预约订单列表（媒介端）行为
    BLP = Booking_listM_Page(init)
    # 实例化B端预约订单列表（媒介端）添加数据截图行为
    ASP = Add_screenshotpage(init)
    yield init, LBP, HBP, BLP, ASP


class Test_B_add_screenshot:
    @pytest.mark.process
    @pytest.mark.usefixtures('b_add_screenshot')
    def test_b_add_screenshot(self, b_add_screenshot):
        # 调用B端登录行为
        b_add_screenshot[1].loginB(success_b_data["username"], success_b_data["password"])
        # B端首页_鼠标悬浮在V代言M元素
        b_add_screenshot[2].mouse_booking_list()
        sleep(1)
        # 点击V_代言M——预约订单列表
        b_add_screenshot[2].click_Booking_list()
        sleep(3)
        # js滚动条-滚动到全部订单可见
        b_add_screenshot[3].js_scroll_all_order()
        sleep(5)
        # 切换至全部订单
        b_add_screenshot[3].click_all_order()
        # 预约订单列表（媒介）-输入需求名称
        b_add_screenshot[3].input_requirement_name(BookingData.booking_name)
        # 预约订单列表（媒介）-查询
        b_add_screenshot[3].click_Query_button()
        # 预约订单列表（媒介）-点击添加/修改数据截图按钮
        b_add_screenshot[3].click_add_screenshot()
        # 添加数据截图弹框_全选
        b_add_screenshot[4].click_all_select()
        # 添加数据截图弹框_先点击上传按钮
        b_add_screenshot[4].operate_upload_cilck()
        sleep(2)
        # 添加数据截图弹框_上传
        b_add_screenshot[4].send_upload_cilck(B_Data.path)
        sleep(2)
        # 添加数据截图弹框_送达人数
        b_add_screenshot[4].operate_send_people(B_Data.delivery_people)
        sleep(2)
        # 添加数据截图弹框_批量提交
        b_add_screenshot[4].operate_batch_submit()
        # 添加数据截图弹框_确认提交
        b_add_screenshot[4].operate_confirm_button()
        # 断言成功提示语
        assert b_add_screenshot[4].get_text_msg() == B_Data.submit_success


if __name__ == '__main__':
    pytest.main()
