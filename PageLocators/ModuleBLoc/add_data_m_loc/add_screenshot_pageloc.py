"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 7:57
"""

from selenium.webdriver.common.by import By

'''B端媒介添加/修改数据截图弹框页面行为'''


class ADD_screenshotLoc:
    # 添加/修改数据截图-全选
    all_select = (By.XPATH, '//div[@tabindex="-1"][last()]//thead//input[@type="checkbox"]')
    # 添加/修改数据截图-上传操作
    upload_cilck = (By.XPATH, '//div[@tabindex="-1"][last()]//span[text()="上传"]')
    # 添加/修改数据截图-送达人数
    # send_people = (By.XPATH, '//div[@tabindex="-1"][last()]//dd/div[1]')
    send_people = (By.XPATH, '//div[@tabindex="-1"][last()]//span[text()="送达人数"]/following::input')
    # 添加/修改数据截图-批量提交
    batch_submit = (By.XPATH, '//div[@tabindex="-1"][last()]//span[text()="批量提交"]')
    # 添加/修改数据截图-确定按钮
    confirm_button = (By.XPATH, '//span[text()="确定"]')
    # 添加/修改数据截图-提交成功
    submit_success_msg = (By.XPATH, '//span[text()="提交成功"]')
