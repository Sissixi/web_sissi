"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/22 0022 上午 10:30
"""
'''创建预约活动需求填写页面--元素定位'''

from selenium.webdriver.common.by import By


class FillFormPageLoc:
    # 预约需求名称元素定额
    name = (By.ID, 'name')
    # 预计推广起始时间
    start_time = (By.ID, "start_time")
    # 预计推广结束时间
    end_time = (By.ID, 'end_time')
    # 预约结果反馈时间
    feedback_time = (By.ID, 'media_feedback_time_expected')
    # 请选择按钮
    select_button = (By.XPATH, '//a[@class="button btn_middle_important js_spread_trade"]//span[@class="btn_wrap"]')
    # 美妆日化行业定位
    trade_button = (By.XPATH, "//em[text()='美妆日化']")
    # 下一步元素定位
    next_button = (By.XPATH, '//a[@id="submitButton"]')
    # 预约需求描述元素定位
    # 定位到iframe中
    description = (By.XPATH, '//iframe[@id="ueditor_0"]')
