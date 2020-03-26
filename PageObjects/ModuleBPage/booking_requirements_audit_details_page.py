#coding:utf-8
from Commons.basepage import BasePage
from PageLocators.ModuleBLoc.booking_requirements_audit_details_pageloc import Booking_requirements_AuditLoc as loc
'''
B端-预约需求详情-审核页面行为
'''
class Review_detailsPage(BasePage):
    def click_check_comment(self):
        self.click_element(loc.Reservation_requirements,"预约需求详情_预约需求基本信息审核通过")

    def confirm_bounced(self):
        self.operation_popout_confirm("审核页面预约需求审核通过_确认弹框")
    def confirm_pop_up(self):
        self.click_element(loc.confirm_button,"预约需求审核页面审核通过后_点击提示弹框的确定按钮")
    def click_handle_js(self):
        self.js_scrollIntoView(loc.Suggest_modify,"预约需求审核页面预约订单列表_滚动条到底部")
    def click_auide_all(self):
        self.click_element(loc.auide_all,"预约需求审核页面预约订单列表_全选")
    def click_batch_auide_pass(self):
        self.click_element(loc.batch_auide_pass,"预约需求审核页面预约订单列表_点击批量审核通过按钮")


