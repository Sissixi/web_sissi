import os
import time, datetime
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
# driver.get("http://toufang.tst-weiboyi.com:8080/\
# pack/reservationrequirement/orderlistformedia/time_type/1\
# /start_time//end_time//company_name//requirement_name/webzdh/requirement_id//\
# order_id//reservation_status//order_first_review_status/10/order_execution_review_status\
# //weibo_name//sale_manager_id//plan_manager_id//has_screenshot_with_execution_result//\
# doc_type//customer_confirmation_status//execution_status//owner_admin_id//identity_name\
# //is_customer_specified//is_prepayment//prepayment_status//prepayment_result//\
# is_self_created//response_reservation_app_id//execution_operate_app_id//renege//\
# execution_status_sub//upload_execution_img_app_id//check_spend_start_hour//\
# check_spend_start_minute//check_spend_end_hour//check_spend_end_minute\
# //response_spend_start_hour//response_spend_start_minute//response_spend_end_hour//response_spend_end_minute//level_id//public_advance_payment_apply_status//last_payment_status//order_by_reservation_order_checked_spend_time//order_by_response_reservation_spend_time//special_type/1/weibo_type_filter//")
# driver.find_element(By.ID, "username").send_keys("hanyi")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.TAG_NAME, 'button').click()
# time.sleep(10)
# driver.find_element(By.CLASS_NAME, "AcceptReservationBrief").click()
# time.sleep(1)
# # 1.实例化select类--提供select定位元素对象
# loc = (By.ID, 'with_topic_and_link')
# # 等待select元素可见
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
# # 找到select元素
# select_ele = driver.find_element(*loc)
# # 实例化select类
# s = Select(select_ele)
# time.sleep(1)
# s.select_by_visible_text('是')
# time.sleep(1)
# #应约按钮
# driver.find_element(By.XPATH, '//*[@id="weiboyiCmp79"]//label[@class="replay_reservation"]').click()
# time.sleep(1)
#
# body = "嘻嘻嘻哈哈哈啊"
#
# # js处理iframe问题
# js = 'document.getElementById("ueditor_0").contentWindow.document.body.innerHTML="{}"'.format(body)
# driver.execute_script(js)
# time.sleep(2)
# #提交按钮
# driver.find_element(By.XPATH, '//*[contains(@id,"weiboyiCmp")]//a[contains(@class,"btn_small_important")]').click()
# time.sleep(2)
#
# driver.quit()
print(time.strftime("%Y-%m-%d"))