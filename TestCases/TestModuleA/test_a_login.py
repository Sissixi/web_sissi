"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 10:19
"""
import pytest
from time import sleep
from TestDatas.Commons_datas import base_a_url
from PageObjects.ModuleAPage.login_a_page import Logina
from TestDatas.ModuleADatas.login_a_datas import success_a_data, fail_a_data, data
from PageObjects.ModuleAPage.home_a_page import HomePage

'''A端登录'''


@pytest.fixture
def init_a(init):
    # 获取A端登录地址
    init.get(base_a_url)
    # 实例化A端登录行为
    la = Logina(init)
    yield init, la


# 代表这个类下面的每一条测试用例都用这个前置
# @pytest.mark.usefixtures("init_a")
# class TestALogin:
#     def test_login_a_success(self, init_a):  # init_a代表返回的(driver,la)
#         '''A端登录页面，登录成功操作'''
#         init_a[1].login_form(success_a_data["username"], success_a_data["password"], success_a_data["code"])
#         sleep(1)
#         # 判断首页-创建活动按钮是否存在
#         assert (HomePage(init_a[0]).button_is_exist()) is True
#
#     @pytest.mark.parametrize("datas", fail_a_data)
#     def test_login_a_fail(self, init_a, datas):
#         '''A端登录，登录失败弹框提示'''
#         init_a[1].login_form(datas["username"], datas["password"], datas["code"])
#         sleep(1)
#         assert init_a[1].login_fail_msg() == datas["check"]
#
#     def test_login_a_fail_code_None(self, init_a):
#         '''A端登录，验证码错误提示'''
#         init_a[1].login_form(data["username"], data["password"], data["code"])
#         sleep(1)
#         assert init_a[1].login_code_none_msg() == data["check"]
#
#
# if __name__ == '__main__':
#     pytest.main()
