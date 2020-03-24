# coding:utf-8
from selenium.webdriver.common.by import By

'''
B端预约订单列表媒介-应约弹框-应约回复/价格信息页面元素定位
'''


class accept_popLoc:
    # 应约备注处-可带要求的话题/@/链接下拉框
    top_link = (By.ID, 'with_topic_and_link')
    # 直发报价-应约按钮
    accept_button = (By.XPATH, '//*[@id="weiboyiCmp79"]//label[@class="replay_reservation"]')
    # 应约回复
    # 定位到iframe中
    accept_reply = (By.XPATH, '//iframe[contains(@id,"ueditor_")]')
    # 应约回复输入内容框
    accept_content = (By.XPATH, '//body[@class="view"]/p[1]/span[1]')
    # 提交按钮
    button = (By.XPATH, '//*[contains(@id,"weiboyiCmp")]//a[contains(@class,"btn_small_important")]')
    # 二次确认弹框
    confirm_button = (By.XPATH, '//*[@id="weiboyiConfirmWin"]//a[@class="btn_small_strong weiboyiWindow_btn button"]')
