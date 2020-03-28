"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 下午 4:06
"""
'''A端提交已选账号页面-元素定位'''
from selenium.webdriver.common.by import By


class Account_submitPage:
    # 全选按钮
    check_all = (By.XPATH, '//input[@class="js_select_all"]')
    # 点击批量添加订单信息按钮并提交
    order_msg_button = (By.XPATH, '//span[text()="批量添加订单信息并提交"]')
    # 提示框确认按钮
    prompt_msg = (By.XPATH, '//div[@class="weiboyiWindow_foot"]//span[text()="确定"]')
    '''添加订单信息并提交弹框'''
    # 合作形式-直发
    straight_button = (By.XPATH, '//input[@value="30"]')
    # 合作形式-转发
    transpond_button = (By.XPATH, '//input[@value="31"]')
    # 合作形式-其他
    other_button = (By.XPATH, '//input[@value="32"]')
    # 需求描述-先切换到iframe表单中
    requirement_description = (By.XPATH, '//iframe[@id="ueditor_0"]')
    #需求描述—防屏蔽文本定位
    shielding=(By.XPATH, '//p[contains(text(),"1）防屏蔽")]')
    # 点击保存并提交按钮
    save_button = (By.XPATH, '//a[contains(@class,"weiboyiWindow_btn")]//span[text()="保存并提交"]')
    # 二次确认按钮元素定位
    confirm_button = (By.XPATH, '//a[contains(@class,"weiboyiWindow_btn")]//span[text()="确定"]')
    # 查看已提交活动按钮
    view_button = (By.XPATH, '//a[contains(@class,"weiboyiWindow_btn")]//span[text()="查看已提交活动"]')
