"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/4/1 0001 上午 10:56
"""
import pytest
from time import sleep
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleNBPage.home_nb_page import HomeNbPage
from PageObjects.ModuleNBPage.quality_list_nb_page import QualityListPage
from PageObjects.ModuleNBPage.quality_nb_page import QualityNbPage
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from TestDatas.Commons_datas import base_nb_url
from TestDatas.ModuleBDatas.login_b_datas import success_b_data
from TestDatas.ModuleNBDatas import quality_datas

'''
NB端质检申诉操作-同意质检结果
'''


@pytest.fixture
def init_nb_quality(init):
    init.get(base_nb_url)
    # 实例化NB登录
    LBP = LoginBPage(init)
    # 实例化NB首页
    HBP = HomeNbPage(init)
    # 实例化质检列表
    QLP = QualityListPage(init)
    # 实例化质检页面
    QNP = QualityNbPage(init)
    yield init, LBP, HBP, QLP, QNP


class Test_NB_Quality_process:
    @pytest.mark.process
    @pytest.mark.usefixtures('init_nb_quality')
    def test_nb_qua_pro(self, init_nb_quality):
        # 登录NB
        init_nb_quality[1].loginB(success_b_data["username"], success_b_data["password"])
        # 点击首页左下角折叠按钮
        init_nb_quality[2].click_folding_layer()
        # 点击首页质检管理
        init_nb_quality[2].click_quality_manage()
        # nb首页_点击nb首页_点击质检管理
        init_nb_quality[2].click_booking_quality_manage()
        sleep(2)
        # 关闭首页左下角折叠按钮
        init_nb_quality[2].click_close_layer()
        #质检列表-点击重置搜索框按钮
        init_nb_quality[3].click_resetFilter()
        sleep(2)
        # 质检列表-输入账号名称
        init_nb_quality[3].click_input_name(BookingData.account_name)
        # 质检列表-搜索
        init_nb_quality[3].click_search_button()
        sleep(2)
        # 质检列表-等待批量质检合格元素处理可见
        init_nb_quality[3].js_scroll()
        sleep(2)
        #nb质检列表_鼠标悬停申诉按钮
        init_nb_quality[3].click_mouse_actions()
        sleep(5)
        # nb质检页面_确认同意质检结果
        init_nb_quality[4].click_allow_quality()
        sleep(1)
        # nb质检页面_再次确认同意质检结果
        init_nb_quality[4].click_confirm_allow_quality()
        sleep(5)

if __name__ == '__main__':
    pytest.main()