"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/22 0022 下午 7:47
"""

import json
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller as c2
from pynput.mouse import Button, Controller as c1
#
#
# class vcg_get_cookies():
#     mouse = c1()
#     url = 'http://qudao.tst-weiboyi.com/auth/user/#/login'
#     options = webdriver.ChromeOptions()
#     # 不加载图片,加快访问速度
#     options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
#     # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
#     options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     # 添加本地代理
#     # options.add_argument("--proxy--server=127.0.0.1:8080")
#     # 添加UA
#     ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
#     options.add_argument('user-agent=' + ua)
#
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     wait = WebDriverWait(driver, 10)
#     driver.get(url)
#     time.sleep(3)
#     driver.refresh()
#     driver.find_element(By.ID, "login_username").send_keys("Sissi123")
#     driver.find_element(By.ID, "login_password").send_keys("wby123456")
#     time.sleep(1)
#     while True:
#         # pyautogui.press('f5')
#         # keyboard.press(Key.f5)
#
#         time.sleep(3)
#         mouse.position = (890, 485)
#         mouse.press(Button.left)
#         mouse.move(1160, 485)
#         mouse.release(Button.left)
#         time.sleep(3)
#         WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//div[@id="nc_1__scale_text"]/span')))
#         if driver.find_element_by_xpath('//div[@id="nc_1__scale_text"]/span').text == '验证通过':
#             break


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


