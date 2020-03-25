import os
import time, datetime
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
# class BasePage:
#     def __init__(self, drive: WebDriver):
#         self.driver = drive
#
#     def wait_ele_visable(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         等待元素可见
#         :param loc: 元素定位
#         :param img_doc:那个页面那个行为
#         :param timeout:等待时间默认20秒
#         :param poll_frequency:间隔默认0.5
#         :return:
#         '''
#         do_log.info(f"等待元素{loc}可见")
#         # 开始等待时间
#         star_time = datetime.datetime.now()
#         try:
#             WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
#         except:
#             do_log.exception(f"等待元素{loc}可见失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             end_time = datetime.datetime.now()
#             do_log.info(f"起始等待时间{star_time},结束等待时间{end_time},共等待时间为{end_time - star_time}")
#
#     def _save_page_shot(self, img_doc):
#         '''
#         截图封装
#         :param img_doc: 那个页面那个行为
#         :return:
#         '''
#         # 获取截图后缀时间
#         time_PNG = time.strftime("%Y-%m-%d %H_%M_%S")
#         # 获取截图文件名称,不能包含：/空格等字符
#         page_name = f"{img_doc}_{time_PNG}.png"
#         # 日志记录
#         do_log.info(f"截图文件存放在{page_name}中")
#         # 获取截图存放路径
#         file_path = os.path.join(SCREEN_PATH, page_name)
#         try:
#             self.driver.save_screenshot(file_path)
#         except:
#             do_log.exception("保存截图失败")
#         else:
#             do_log.info("保存截图成功")
#
#     def get_element(self, loc, img_doc):
#         '''
#         查找元素封装
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :return:返回找到的元素
#         '''
#         do_log.info(f"{img_doc}查找元素{loc}")
#         try:
#             ele = self.driver.find_element(*loc)
#         except:
#             do_log.exception(f"查找元素{loc}失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info(f"查找元素{loc}成功")
#             return ele
#
#     def click_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         点击操作
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}点击{loc}元素")
#         try:
#             ele.click()
#         except:
#             do_log.exception(f"{img_doc}点击{loc}元素失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#
#     def clear_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         清除操作
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}清除{loc}元素")
#         try:
#             ele.clear()
#         except:
#             do_log.exception(f"{img_doc}清除{loc}元素失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#
#     def input_text(self, loc, text, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         输入操作
#         :param loc:
#         :param text:输入的文本
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}在{loc}输入文本值:{text}")
#         try:
#             ele.send_keys(text)
#         except:
#             do_log.exception("输入文本值失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info("输入文本值成功")
#
# class BasePage:
#     def __init__(self, drive: WebDriver):
#         self.driver = drive
#
#     def wait_ele_visable(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         等待元素可见
#         :param loc: 元素定位
#         :param img_doc:那个页面那个行为
#         :param timeout:等待时间默认20秒
#         :param poll_frequency:间隔默认0.5
#         :return:
#         '''
#         do_log.info(f"等待元素{loc}可见")
#         # 开始等待时间
#         star_time = datetime.datetime.now()
#         try:
#             WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
#         except:
#             do_log.exception(f"等待元素{loc}可见失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             end_time = datetime.datetime.now()
#             do_log.info(f"起始等待时间{star_time},结束等待时间{end_time},共等待时间为{end_time - star_time}")
#
#     def _save_page_shot(self, img_doc):
#         '''
#         截图封装
#         :param img_doc: 那个页面那个行为
#         :return:
#         '''
#         # 获取截图后缀时间
#         time_PNG = time.strftime("%Y-%m-%d %H_%M_%S")
#         # 获取截图文件名称,不能包含：/空格等字符
#         page_name = f"{img_doc}_{time_PNG}.png"
#         # 日志记录
#         do_log.info(f"截图文件存放在{page_name}中")
#         # 获取截图存放路径
#         file_path = os.path.join(SCREEN_PATH, page_name)
#         try:
#             self.driver.save_screenshot(file_path)
#         except:
#             do_log.exception("保存截图失败")
#         else:
#             do_log.info("保存截图成功")
#
#     def get_element(self, loc, img_doc):
#         '''
#         查找元素封装
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :return:返回找到的元素
#         '''
#         do_log.info(f"{img_doc}查找元素{loc}")
#         try:
#             ele = self.driver.find_element(*loc)
#         except:
#             do_log.exception(f"查找元素{loc}失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info(f"查找元素{loc}成功")
#             return ele
#
#     def click_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         点击操作
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}点击{loc}元素")
#         try:
#             ele.click()
#         except:
#             do_log.exception(f"{img_doc}点击{loc}元素失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#
#     def clear_element(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         清除操作
#         :param loc: 元素定位
#         :param img_doc: 截图
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}清除{loc}元素")
#         try:
#             ele.clear()
#         except:
#             do_log.exception(f"{img_doc}清除{loc}元素失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#
#     def input_text(self, loc, text, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         输入操作
#         :param loc:
#         :param text:输入的文本
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}在{loc}输入文本值:{text}")
#         try:
#             ele.send_keys(text)
#         except:
#             do_log.exception("输入文本值失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info("输入文本值成功")
#
#     def get_text(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         获取文本
#         :param loc:
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:返回文本
#         '''
#         # 1.等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}获取元素{loc}文本值")
#         try:
#             value = ele.text
#         except:
#             do_log.exception(f"{img_doc}获取元素{loc}文本值失败")
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info(f"元素文本值为{value}")
#             return value
#
#     def get_ele_attribute(self, loc, attr_name, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         获取元素属性值
#         :param loc:
#         :attr_name:元素的属性名
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return: 返回元素属性值
#         '''
#         # 1.等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}获取元素{loc}属性值为{attr_name}")
#         try:
#             value = ele.get_attribute(attr_name)
#         except:
#
#             do_log.exception(f"{img_doc}获取元素{loc}属性值失败")
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info(f"{img_doc}获取元素{loc}属性值为{attr_name}")
#             return value
#
#     def get_windows_handles(self):
#         '''
#         获取所有窗口列表
#         :return:
#         '''
#         do_log.info("获取所有窗口列表")
#         try:
#             wins = self.driver.window_handles
#         except:
#             do_log.exception("获取所有窗口列表失败")
#             raise
#         else:
#             do_log.info(f"获取所有窗口列表成功，窗口列表为{wins}")
#             return wins
#
#     def switch_to_new_window(self):
#         '''
#         获取最新窗口列表
#         :return:
#         '''
#         # 切换窗口，要等待2秒
#         time.sleep(2)
#         # 获取所有窗口
#         wins = self.get_windows_handles()
#         do_log.info("切换到当前最新的窗口")
#         try:
#             self.driver.switch_to.window(wins[-1])
#         except:
#             do_log.exception("切换最新窗口失败")
#             raise
#
#     def check_ele_visiable(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         检测元素是否在页面存在且可见，如果元素存在，返回True,否则返回False
#         :param loc:
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         do_log.info(f"{img_doc}:检测元素{loc}存在且可见于页面")
#         try:
#             WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
#         except:
#             do_log.exception(f"{timeout}秒元素在当前页面不可见")
#             self._save_page_shot(img_doc)
#             return False
#         else:
#             do_log.info(f"{timeout}秒内元素可见")
#             return True
#
#     def switch_to_iframe(self, iframe_pref, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         iframe切换
#         判断frame是否可用，如果可用则返回True并切入到该frame，
#         参数iframe_pref可以是定位器locator也就是（by,xpath）组成的元组，
#         或者定位方法：ID、name、index(该frame在页面上的索引号)，或WebElement对象
#         '''
#         try:
#             WebDriverWait(self.driver, timeout).until(
#                 EC.frame_to_be_available_and_switch_to_it(iframe_pref))
#         except:
#             do_log.exception(f"切换{img_doc}的iframe元素{iframe_pref}失败!")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info(f"切换{img_doc}的iframe元素成功!可对新的html页面操作")
#
#     def back_iframe(self, img_doc):
#         try:
#             self.driver.switch_to.default_content()
#         except:
#             do_log.exception("返回到主iframe失败")
#             self._save_page_shot(img_doc)
#
#     def js_time(self, loc, timevalue, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         js处理日历控件
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见元素
#         self.get_element(loc, img_doc)
#         do_log.info(f"通过js语句修改元素{loc}的时间")
#         try:
#             js_pha = f'var a=document.getElementById({loc});a.value="{timevalue}";'
#             self.driver.execute_script(js_pha)
#         except:
#             do_log.exception(f"通过js语句修改元素{loc}失败")
#             # 截图
#             self._save_page_shot(img_doc)
#         else:
#             do_log.info(f"通过js语句修改元素{loc}成功")
#
#     def input_key_text(self, loc, keymethod, img_doc, timeout=20, poll_frequency=0.5):
#         '''
#         鼠标操作
#         :param loc:
#         :param text:输入的文本
#         :param img_doc:
#         :param timeout:
#         :param poll_frequency:
#         :return:
#         '''
#         # 1.先等待元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的元素
#         ele = self.get_element(loc, img_doc)
#         try:
#             ele.send_keys(keymethod)
#         except:
#             do_log.exception("输入失败")
#             # 截图
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             do_log.info("输入成功")
#
#     def popout(self):
#         '''
#         切换到alert弹框
#         :return:
#         '''
#         try:
#
#             al = self.driver.switch_to.alert
#         except:
#             do_log.exception("切换到弹框内失败")
#             raise
#         else:
#             return al
#
#     def operation_popout_confirm(self, img_doc):
#         '''
#         点击弹框中的确定按钮
#         :return:
#         '''
#         al = self.popout()
#         do_log.info("切换到弹框内")
#         try:
#             al.accept()
#         except:
#             do_log.exception("点击弹框中的确定按钮失败")
#             self._save_page_shot(img_doc)
#             raise
#
#     def operation_popout_text(self, img_doc):
#         '''
#         获取弹框中的文本内容
#         :return:
#         '''
#         al = self.popout()
#         do_log.info("切换到弹框内")
#         try:
#             # 获取弹框中的文本内容
#             content = al.text
#         except:
#             do_log.exception("获取弹框中的文本内容失败")
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             # 返回弹框中文本内容
#             return content
#
#     def mouse_action(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''鼠标操作-鼠标悬浮'''
#         try:
#             # 1.实例化action_chains
#             ac = ActionChains(self.driver)
#             time.sleep(1)
#             # 2.将要操作的动作放在链表中
#             ele = self.get_element(loc, img_doc)
#             time.sleep(1)
#             # 设置鼠标悬浮
#             ac.move_to_element(ele)
#             # 鼠标即悬浮又点击
#             # ac.move_to_element(ele).click(ele)
#             # 3.调用perform()
#             ac.perform()
#         except:
#             do_log.exception("设置鼠标悬停失败")
#             self._save_page_shot(img_doc)
#             raise
#
#     def mouse_drag_and_drop_by_offset(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''鼠标操作拖拽'''
#         pass
#
#     def drop_down_box(self, loc, img_doc, timeout=20, poll_frequency=0.5):
#         '''下拉框操作_实例化select类'''
#         # 1.先等待select元素可见
#         self.wait_ele_visable(loc, img_doc)
#         # 2.找到可见的select元素
#         ele = self.get_element(loc, img_doc)
#         do_log.info(f"{img_doc}找到{loc}元素")
#         try:
#             # 实例化select类
#             s = Select(ele)
#             # 获取下拉列表的值
#         except:
#             do_log.exception("实例化select类失败")
#             self._save_page_shot(img_doc)
#             raise
#         else:
#             return s
#
#     def select_value(self, loc, text_value, img_doc, timeout=20, poll_frequency=0.5):
#         '''下拉操作_获取下拉列表的值，根据文本值获取'''
#         try:
#             # 根据下拉列表的文本值获取下拉列表的值，text_value代表文本值
#             self.drop_down_box(loc, img_doc).select_by_visible_text(text_value)
#         except:
#             do_log.exception("获取下拉列表的文本值失败")
#             self._save_page_shot(img_doc)
#             raise
#     def keys_click(self,loc, text_value, img_doc, timeout=20, poll_frequency=0.5):
#         '''键盘操作全选'''
#         pass
#
#
#
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://toufang.tst-weiboyi.com:8080/pack/reservationrequirement/orderlistformedia/time_type/1/start_time//end_time//company_name//requirement_name/webzdh/requirement_id//order_id//reservation_status//order_first_review_status/10/order_execution_review_status//weibo_name//sale_manager_id//plan_manager_id//has_screenshot_with_execution_result//doc_type//customer_confirmation_status//execution_status//owner_admin_id//identity_name//is_customer_specified//is_prepayment//prepayment_status//prepayment_result//is_self_created//response_reservation_app_id//execution_operate_app_id//renege//execution_status_sub//upload_execution_img_app_id//check_spend_start_hour//check_spend_start_minute//check_spend_end_hour//check_spend_end_minute//response_spend_start_hour//response_spend_start_minute//response_spend_end_hour//response_spend_end_minute//level_id//public_advance_payment_apply_status//last_payment_status//order_by_reservation_order_checked_spend_time//order_by_response_reservation_spend_time//special_type/1/weibo_type_filter//")
#     bp = BasePage(driver)
#     bp.input_text((By.ID, "username"), "hanyi", "用户名输入")
#     bp.input_text((By.ID, "password"), "123456", "密码输入")
#     bp.click_element((By.TAG_NAME, 'button'), "登录按钮")
#     time.sleep(1)
#     bp.click_element((By.CLASS_NAME,"AcceptReservationBrief"), "应约按钮")
#     time.sleep(1)
#     bp.select_value((By.ID, 'with_topic_and_link'),"是", "应约弹框_应约备注_带要求的话题/@/链接")
#     bp.click_element((By.XPATH, '//*[@id="weiboyiCmp79"]//label[@class="replay_reservation"]'),"应约")
#     ele = bp.click_element((By.XPATH, "//div[@class='weiboyiWindow absoluteCenter'][last()]//iframe"), "应约弹框_应约回复输入框")
#     bp.switch_to_iframe(ele, "切换iframe_应约回复输入框")
#     time.sleep(15)
#
#     bp.clear_element((By.TAG_NAME, "body"), "应约回复输入框输入")
#     time.sleep(1)
#     bp.input_text((By.TAG_NAME, "body"), "应约回复test", "应约回复输入框输入")
#
#     time.sleep(1)


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://toufang.tst-weiboyi.com:8080/\
pack/reservationrequirement/orderlistformedia/time_type/1\
/start_time//end_time//company_name//requirement_name/webzdh/requirement_id//\
order_id//reservation_status//order_first_review_status/10/order_execution_review_status\
//weibo_name//sale_manager_id//plan_manager_id//has_screenshot_with_execution_result//\
doc_type//customer_confirmation_status//execution_status//owner_admin_id//identity_name\
//is_customer_specified//is_prepayment//prepayment_status//prepayment_result//\
is_self_created//response_reservation_app_id//execution_operate_app_id//renege//\
execution_status_sub//upload_execution_img_app_id//check_spend_start_hour//\
check_spend_start_minute//check_spend_end_hour//check_spend_end_minute\
//response_spend_start_hour//response_spend_start_minute//response_spend_end_hour//response_spend_end_minute//level_id//public_advance_payment_apply_status//last_payment_status//order_by_reservation_order_checked_spend_time//order_by_response_reservation_spend_time//special_type/1/weibo_type_filter//")
driver.find_element(By.ID, "username").send_keys("hanyi")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(10)
driver.find_element(By.CLASS_NAME, "AcceptReservationBrief").click()
time.sleep(1)
# 1.实例化select类--提供select定位元素对象
loc = (By.ID, 'with_topic_and_link')
# 等待select元素可见
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
# 找到select元素
select_ele = driver.find_element(*loc)
# 实例化select类
s = Select(select_ele)
time.sleep(1)
s.select_by_visible_text('是')
time.sleep(1)
#应约按钮
driver.find_element(By.XPATH, '//*[@id="weiboyiCmp79"]//label[@class="replay_reservation"]').click()

#使用js滑动到应约回复可见区域
driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element(By.XPATH, "//div[@class='weiboyiWindow absoluteCenter'][last()]//iframe"))
time.sleep(3)
#切换进应约回复iframe框
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='weiboyiWindow absoluteCenter'][last()]//iframe"))
time.sleep(2)
#使用js滑动到应约回复可见区域body处
driver.execute_script("arguments[0].scrollIntoView(false);", driver.find_element(By.TAG_NAME, "body"))
time.sleep(1)
#先点击body处
driver.find_element(By.TAG_NAME, "body").click()
time.sleep(1)
#driver.find_element(By.TAG_NAME, "body").send_keys(Keys.DELETE)
#找到body处P内的元素，随便清除一个
driver.find_elements(By.TAG_NAME,"p")[1].send_keys(Keys.DELETE)
time.sleep(1)
#找到body处P内的元素，输入内容
driver.find_elements(By.TAG_NAME,"p")[1].send_keys("应约回复输入框输入")
time.sleep(1)
driver.switch_to.default_content()
#提交按钮
driver.find_element(By.XPATH, '//*[contains(@id,"weiboyiCmp")]//a[contains(@class,"btn_small_important")]').click()
pass
driver.quit()