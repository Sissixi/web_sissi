"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/30 0030 下午 3:12
"""
from selenium.webdriver.common.by import By

'''B端媒介添加执行结果弹框页面行为'''


class Add_execution_resultsLoc:
    # 添加执行结果弹框全选按钮
    all_selecet = (By.XPATH, '//div[@class="weiboyiWindow absoluteCenter"]//input[@type="checkbox"]')
    # 添加执行结果-执行链接
    perform_link = (By.XPATH, '//div[@class="weiboyiWindow absoluteCenter"]//input[@type="text"]')
    # 添加执行结果-上传图片
    upload_pictures = (By.XPATH,'//div[@class="weiboyiWindow absoluteCenter"]//span[text()="上传"]')
    # 添加执行结果-批量提交
    batch_submit = (By.XPATH, '//div[@class="weiboyiWindow absoluteCenter"]//span[text()="批量提交"]')
    # 确定按钮
    confirm_button = (By.XPATH, '//span[text()="确定"]')
    # 提交执行结果成功
    success_msg = (By.XPATH, '//span[text()="执行结果提交成功"]')
