# coding:utf-8
from selenium.webdriver.common.by import By

'''
B端预约订单列表媒介页面元素定位
'''


class Booking_listLoc:
    # 需求名称输入框
    requirement_name = (By.XPATH, '//input[@name="requirement_name"]')
    # 查询按钮
    Query_button = (By.ID, "order_search")
    # 应约按钮
    accept_button = (By.CLASS_NAME, "AcceptReservationBrief")
    # 应约成功提示
    accept_success_msg = (By.XPATH, '//span[text()="应约成功，订单状态变为执行中后方可执行"]')
    # 全部订单tab
    all_order = (By.XPATH, '//ul[@id="tabChangeBox"]/li[1]')
    # 添加执行结果
    add_result = (By.XPATH, '//a[@class="addExecutionResult"]')
    # 添加修改数据截图
    add_screenshot = (By.XPATH, '//a[@class="addDataScreenshot"]')
