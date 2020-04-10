"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/31 0031 下午 10:58
"""
from selenium.webdriver.common.by import By

'''
NB端质检列表页面元素定位
'''


class QualityListPageLoc:
    #重置搜索框
    resetFilter_button=(By.CLASS_NAME,"resetFilter")
    # 质检状态元素-请选择class定位
    quality_status = 'ant-select-selection-selected-value'
    # 详细质检状态内去掉默认元素定位
    not_check = (By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]')
    # 修改详细质检状态-未检元素定位
    js1 = "ant-select-selection__choice__content"
    js2 = "ant-select-selection__choice"
    # 账号名称输入框
    input_name = (By.XPATH, '//input[@id="weibo_name"]')
    # 搜索按钮
    search_button = (By.XPATH, '//div[@class="ant-spin-container"]//button[@class="ant-btn ant-btn-primary"]')
    # 批量质检合格元素
    batch_qualified = (By.XPATH, '//button[@class="ant-btn batchTips ant-btn-default"]')
    # 全选按钮
    all_select_button = (By.XPATH, '//div[@class="reservationTable"]//div[@class="ant-table-footer"]//span[1]//input[@type="checkbox"]')
    # 处理/申诉按钮
    dispose_button = (By.XPATH,'//div[@class="ant-table-body-inner"]//tbody[@class="ant-table-tbody"]/tr[last()]//button')
