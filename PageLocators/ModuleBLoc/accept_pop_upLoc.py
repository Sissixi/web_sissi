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
    # 定位到iframe中,//div[@class='weiboyiWindow absoluteCenter']代表定位到弹框；[last()]代表最后一个class
    accept_reply = (By.XPATH, "//div[@class='weiboyiWindow absoluteCenter'][last()]//iframe")
    # 应约回复-定位到iframe内的body标签处
    accept_body = (By.TAG_NAME, "body")
    # 应约回复-定位到iframe内的body标签下的p元素中的任意一个
    accept_body_p = (By.TAG_NAME, "p")[1]
    # 提交按钮
    button = (By.XPATH, '//*[contains(@id,"weiboyiCmp")]//a[contains(@class,"btn_small_important")]')
    # 二次确认弹框
    confirm_button = (By.XPATH, '//*[@id="weiboyiConfirmWin"]//a[@class="btn_small_strong weiboyiWindow_btn button"]')
