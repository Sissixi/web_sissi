"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/21 0021 下午 11:17
"""
from selenium.webdriver.common.by import By

'''选择投放平台页面'''


class SelectPage:
    # 挑选投放平台--微博
    select_weibo_platform = (By.XPATH, '//a[@data-weibo-type="1"]')
    # 微博平台-点击预约按钮定位
    weibo_yuyue = (By.XPATH, '//a[@data-track-prop-is-famous="1" and  @data-track-prop-sort="5"]')
    # 挑选投放平台--视频自媒体
    select_video_platform = (By.XPATH, '//a[@data-weibo-type="video"]')
    # 视频自媒体-点击预约按钮
    video_yuyue = (By.XPATH, '//a[@data-track-prop-is-famous="1" and  @data-track-prop-sort="2"]')
