"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 10:20
"""
import pytest

from selenium import webdriver



@pytest.fixture
def init():
    '''测试用例前置'''
    # 打开浏览器
    driver = webdriver.Chrome()
    # 设置隐性等待
    driver.implicitly_wait(10)
    # 最大化
    driver.maximize_window()
    yield driver
    '''测试用例后置'''
    #退出浏览器，关闭会话
    driver.quit()

