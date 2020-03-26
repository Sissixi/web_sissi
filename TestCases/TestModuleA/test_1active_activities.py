"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/21 0021 下午 8:58
"""
import pytest
import time
from selenium import webdriver
from TestDatas.Commons_datas import base_a_url
from PageObjects.ModuleAPage.home_a_page import HomePage
from PageObjects.ModuleAPage.login_a_page import Logina
from TestDatas.ModuleADatas.login_a_datas import success_a_data
from PageObjects.ModuleAPage.select_active_page import SelectPlat
from PageObjects.ModuleAPage.fill_form_page import FillPage
from TestDatas.ModuleADatas.Booking_activities_datas import BookingData
from PageObjects.ModuleBPage.account_select_page import AccountSelectPage
from PageObjects.ModuleBPage.account_submit_page import AccountSubmitPage

'''A端创建预约活动'''


@pytest.fixture
def create_init():
    '''测试用例前置'''
    # 打开浏览器
    driver = webdriver.Chrome()
    # 设置隐性等待
    driver.implicitly_wait(10)
    # 最大化
    driver.maximize_window()
    # 获取A端登录地址
    driver.get(base_a_url)
    # 实例化A端登录行为
    La = Logina(driver)
    yield driver, La
    '''测试用例后置'''
    driver.quit()


class Test_Activit:
    @pytest.mark.usefixtures("create_init")
    def test_create_activit(self, create_init):
        '''
        A端创建预约活动
        :param create_init: create_init相当于是一个元组（driver, La）
        :return:
        '''
        # 调用A端登录行为
        create_init[1].login_form(success_a_data["username"], success_a_data["password"], success_a_data["code"])
        # 点击首页的创建活动按钮
        HomePage(create_init[0]).click_creat_button()
        # 切换到最新窗口
        HomePage(create_init[0]).new_current()
        # 点击新浪平台
        SelectPlat(create_init[0]).click_sina()
        '''先实例化预约需求表单类'''
        fl = FillPage(create_init[0])
        # 输入预约需求名称
        fl.input_name(BookingData.booking_name)

        # 输入预约需求描述
        fl.input_description(BookingData.description_content)
        # 输入预计推广开始时间
        fl.Execute_start_time(BookingData.start_time)

        # 输入预计推广结束时间
        fl.Execute_end_time(BookingData.end_time)

        # 输入预约结果反馈时间
        fl.Execute_feedback_time(BookingData.feedback_time)

        # 选择推广产品所属行业
        fl.select_trade_button()
        time.sleep(1)

        # 点击下一步
        fl.cilck_next_button()

        '''选择账号页面类实例化'''
        sa = AccountSelectPage(create_init[0])
        # 输入账号名称
        sa.account_input_name(BookingData.account_name)
        # 点击新浪微博账号按钮
        sa.account_seach_button()
        time.sleep(1)
        # 选中搜到的账号
        sa.checkbox_button()
        time.sleep(1)

        # 点击查看并提交按钮
        sa.view_submit()

        '''A端提交已选账号页面类实例化'''
        ASP = AccountSubmitPage(create_init[0])
        # 账号全选
        ASP.all_check()
        # 点击批量添加订单信息按钮
        ASP.order_account_button()
        # 二次确认按钮
        ASP.prompt_msg_button()
        time.sleep(1)
        # 切换到需求描述框
        ASP.switch_form()
        time.sleep(1)
        # 添加订单信息并提交弹框中_需求描述
        ASP.requirement_description_form(BookingData.content_msg)
        time.sleep(1)
        # 返回主iframe
        ASP.back_form_iframe()
        # 点击添加订单信息并提交弹框中_保存并提交按钮
        ASP.save_submit_button()
        # 2次确认弹框按钮
        ASP.save_confirm_button()
        # 查看已提交活动按钮
        ASP.view_button()
        time.sleep(1)


if __name__ == '__main__':
    pytest.main()
