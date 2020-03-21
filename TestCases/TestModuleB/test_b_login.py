"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/23 0023 下午 1:52
"""
import pytest
import time
from selenium import webdriver
from PageObjects.ModuleBPage.login_b_page import LoginBPage
from PageObjects.ModuleBPage.home_b_page import Home_B_Page

from TestDatas.Commons_datas import base_b_url
from TestDatas.ModuleBDatas.login_b_datas import success_b_data


# @pytest.fixture
# def init_b():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(base_b_url)
#
#     yield driver
#     driver.quit()
#
# @pytest.mark.usefixtures("init_b")
# class TestBLogin:
#     def test_login_b_success(self, init_b):
#         '''B端登录页面-登录行为'''
#         # 实例化
#         LBP = LoginBPage(init_b)
#         #调用B端登录
#         LBP.loginB(success_b_data["username"], success_b_data["password"])
#         time.sleep(1)
#         assert (Home_B_Page(init_b).marked_words_exist())is True


if __name__ == '__main__':
    pytest.main()
