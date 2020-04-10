"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/4/1 0001 上午 10:28
"""
from Commons.basepage import BasePage
from PageLocators.ModuleNBLoc.quality_list_nb_pageloc import QualityListPageLoc as loc

'''
NB端质检列表页面行为
'''


class QualityListPage(BasePage):
    def click_resetFilter(self):
        self.click_element(loc.resetFilter_button, "点击重置按钮")

    def click_quality_status(self, num, value, text):
        self.js_alter(loc.quality_status, "nb质检列表_修改质检状态未检", num, value, text)

    def click_not_check(self):
        self.click_element(loc.not_check, "nb质检列表_详细质检状态内去掉默认元素定位")

    def updata_js(self, num, value, text):
        self.js_all_alter("nb质检列表_修改详细质检状态未检", loc.js1, loc.js2, num, value, text)

    def click_input_name(self, text):
        self.input_text(loc.input_name, text, "nb质检列表_输入账号名称")

    def click_search_button(self):
        self.click_element(loc.search_button, "nb质检列表_搜索")

    def js_scroll(self):
        self.js_scrollIntoView(loc.batch_qualified, "nb质检列表_等待批量质检合格元素处理可见")

    def click_mouse_actions(self):
        self.click_mouse_action(loc.dispose_button, click=1, img_doc="nb质检列表_鼠标悬停处理按钮")
