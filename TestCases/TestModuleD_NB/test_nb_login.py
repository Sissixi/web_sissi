"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/31 0031 下午 9:32
"""
import pytest
import time
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleNBPage.home_nb_page import HomeNbPage

from TestDatas.Commons_datas import base_nb_url
from TestDatas.ModuleNBDatas.login_nb_datas import success_b_data
'''
NB端登录
'''

@pytest.fixture
def init_nb(init):
    init.get(base_nb_url)
    yield init


@pytest.mark.usefixtures("init_nb")
class TestNBLogin:
    def test_login_nb_success(self, init_nb):
        '''nB端登录页面-登录行为'''
        # 实例化
        LBP = LoginBPage(init_nb)
        # 调用nB端登录
        LBP.loginB(success_b_data["username"], success_b_data["password"])
        time.sleep(1)
        assert (HomeNbPage(init_nb).nb_exist()) is True


if __name__ == '__main__':
    pytest.main()
