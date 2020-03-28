"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/3/27 0027 下午 9:25
"""
import datetime

'''A端预约活动--预约详情订单--添加执行内容数据'''
# 直发内容
straight_content = "我是A端直发内容"
# A端预约订单详情_选择是否含有视频/直播
select_live_video = "含视频"
# A端预约订单详情_执行开始时间
start_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# A端预约订单详情_执行结束时间
end_time = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
