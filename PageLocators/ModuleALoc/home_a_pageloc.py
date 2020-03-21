"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/21 0021 下午 8:40
"""
from selenium.webdriver.common.by import By

'''A端首页'''


class HomeLoc:
    # 创建活动按钮元素定位
    create_buttom = (By.XPATH, '//a[text()="创建活动"]')
