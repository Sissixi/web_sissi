"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/4/1 0001 上午 10:01
"""
from selenium.webdriver.common.by import By

'''
NB端质检页面元素定位
'''


class QualityPageLoc:
    # 执行结果不合格原因-回填执行链接无效
    link_invalid = (By.XPATH, "//span[text()='回填执行链接无效']/preceding-sibling::span")
    # 扣款比例
    Deduct_percentage = (By.XPATH, '//label[@id="charge_ratio"]/input')
    # 提交按钮
    submit_button = (By.XPATH, '//button[@type="submit"]')
    # 同意质检结果
    allow_quality = (By.XPATH, '//button[@class="ant-btn btn ant-btn-primary"]')
    # 确定同意质检结果
    confirm_allow_quality = (
    By.XPATH, '//div[@class="ant-modal-confirm-btns"]//button[@class="ant-btn ant-btn-primary"]')
