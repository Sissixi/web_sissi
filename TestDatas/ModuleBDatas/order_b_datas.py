"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/16 0016 下午 7:20
"""
from Commons.handle_Path import picture_path

'''B端预约用到的测试数据'''


class B_Data:
    # 应约弹框_应约备注_可带要求的话题/@/链接_选择是
    value_text = '是'
    # 应约弹框_应约回复_内容
    replace_content = "文案不调整"
    # 应约成功提示信息
    success_msg = "应约成功，订单状态变为执行中后方可执行"
    # 添加执行结果--执行链接
    Perform_link = "https://weibo.com/1618051664/IAYJfhprF?type=comment"
    # 添加执行结果--上传执行截图绝对路径
    path = picture_path
    # 添加执行结果成功提示信息
    add_executable = "执行结果提交成功"
    # 添加数据截图弹框_送达人数
    delivery_people = 1000
    # 添加数据截图弹框_提交成功提示
    submit_success = "提交成功"
