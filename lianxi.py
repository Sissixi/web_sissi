import os
import datetime, time
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

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://nb.tst-weiboyi.com/qc/reservation")
time.sleep(1)
driver.find_element(By.ID, "username").send_keys("hanyi")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(5)
# #质检状态选择未检
# js0 = 'var a = document.getElementsByClassName("ant-select-selection-selected-value")[3];a.title="未检";a.innerText="未检";'
# driver.execute_script(js0)
# time.sleep(5)
# # 去掉详细质检状态
# driver.find_element(By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]').click()
# time.sleep(1)
#
# # 详情质检状态设置未检
# js1 = 'var s=document.getElementsByClassName("ant-select-selection__choice__content")[0].innerText="未检";' \
#       'var t=document.getElementsByClassName("ant-select-selection__choice")[0].title="未检";'
# driver.execute_script(js1)
# time.sleep(2)
#重置搜索
driver.find_element(By.CLASS_NAME,"resetFilter").click()
time.sleep(2)
#输入账号名称
driver.find_element(By.XPATH, '//input[@id="weibo_name"]').send_keys("我是娜扎")
time.sleep(2)

#点击搜索按钮
driver.find_element(By.XPATH, '//div[@class="ant-spin-container"]//button[@class="ant-btn ant-btn-primary"]').click()
time.sleep(2)

# #滑到页面底部移动到页面底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)
#等待批量质检合格元素处理可见
loc = (By.XPATH, '//button[@class="ant-btn batchTips ant-btn-default"]')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
#先找到这个元素
element = driver.find_element(*loc)
# 通过js将元素滚动到可视区域之后，在操作
# 执行js语句
#arguments接收外部传的参数element，arguments是个列表；第一个参数是js语句，第二个是用到的参数
driver.execute_script("arguments[0].scrollIntoView(false);", element)
time.sleep(2)
#设置鼠标悬停处理按钮
loc=(By.XPATH,'//div[@class="ant-table-body-inner"]//tbody[@class="ant-table-tbody"]/tr[last()]//button')
# 1.实例化action_chains类
ac = ActionChains(driver)
# 2.将要操作的动作放在链表中
ele = driver.find_element(*loc)
#设置鼠标悬浮
ac.move_to_element(ele)
time.sleep(2)
#鼠标即悬浮又点击
ac.move_to_element(ele).click(ele)
# 3.调用perform()
ac.perform()

time.sleep(6)

driver.quit()
