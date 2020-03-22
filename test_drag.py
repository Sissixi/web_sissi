"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/22 0022 下午 7:47
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 模拟鼠标操作-鼠标拖动-滑动验证码
driver = webdriver.Chrome()
driver.get("http://qudao.tst-weiboyi.com/auth/user/#/login")
driver.maximize_window()
driver.refresh()
driver.find_element(By.ID, "login_username").send_keys("Sissi123")
driver.find_element(By.ID, "login_password").send_keys("wby123456")
sleep(1)
loc=(By.XPATH, '//div[@id="nc_1__scale_text"]/span')
span_background=driver.find_element(*loc)
span_background.click()

# #获取滑动条的size
span_background_size = span_background.size
print(span_background_size)
sleep(1)


# 获取滑块的位置
button = driver.find_element(By.ID,"nc_1_n1z")
button_location = button.location
print(button_location)

# 拖动操作：drag_and_drop_by_offset
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）
x_location = button_location["x"] + span_background_size["width"]

y_location = button_location["y"]
ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()


driver.quit()


