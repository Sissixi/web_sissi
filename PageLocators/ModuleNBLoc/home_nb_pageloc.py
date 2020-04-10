"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/31 0031 下午 9:36
"""
from selenium.webdriver.common.by import By

'''
NB端首页元素定位
'''


class HomeNbLoc:
    # nb元素定位
    nb = (By.XPATH, '//span[text()="NB"]')
    # 定位到左下角折叠按钮
    Folding_layer = (By.XPATH, '//i[@class="anticon anticon-right"]')
    # 关闭折叠
    close_layer = (By.XPATH, '//div[@class="ant-layout-sider-trigger"]')
    # 质检管理
    quality_manage = (By.XPATH, '//span[text()="质检管理"]')
    # nb首页_点击质检管理
    booking_quality_manage = (By.ID, '质检管理$Menu')
