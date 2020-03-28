import os
import datetime
from time import ctime
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Commons.handle_logs import do_log
from Commons.handle_Path import SCREEN_PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://chuanbo.tst-weiboyi.com/hwreservation/order/detail/id/58551#anchor_add_execution_content")
# driver.find_element(By.ID, "username").send_keys("luckyxi")
# driver.find_element(By.ID, "password").send_keys("wbyxixi123")
# driver.find_element(By.ID, "piccode").send_keys("1234")
# driver.find_element(By.CLASS_NAME, 'btn_wrap').click()
#
# # 添加执行内容
# loc = (By.XPATH, '//div[@class="reservation_detail_operate"]//a[@action-type="add"]')
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
# time.sleep(1)
# loc = (By.XPATH, '//tr[@data-module="content"]/td/textarea')
# driver.find_element(*loc).click()
# time.sleep(1)
# js1 = 'var a =document.getElementsByClassName("js_content")[0];a.value="xixixixi"'
# driver.execute_script(js1)
# time.sleep(10)
#
# driver.quit()
name=(datetime.datetime.now()+datetime.timedelta(days=5)).strftime("%Y-%m-%d")
print(name)