# coding:utf-8
from selenium.webdriver.common.by import By

'''
B端-预约需求详情-审核页面元素定位
'''


class Booking_requirements_AuditLoc:
    # 预约需求审核通过
    Reservation_requirements = (By.XPATH, '//a[text()="审核通过"]')
    # 预约订单列表-全选框
    auide_all = (By.XPATH, '//input[@name="selectedAll"]')
    # 批量审核通过-按钮
    batch_auide_pass = (By.XPATH, '//a[text()="批量审核通过"]')
    # 审核通过-提示框中的确认弹框按钮中的确定
    confirm_button = (By.XPATH, '//span[text()="确定"]')
    # 预约订单列表-单个订单的审核通过
    auide_pass = (By.XPATH, '//table[@id="report"]//a[text()="审核通过"]')
    #预约订单列表-批量建议修改
    Suggest_modify=(By.XPATH,'//a[text()="批量建议修改"][last()]')