"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 8:37
"""

import os

# 设置项目跟路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# OUtputs文件夹路径
OUTPUTS = os.path.join(BASE_PATH, 'Outputs')
# 设置输出日志文件夹路径
LOGS_PATH = os.path.join(OUTPUTS, 'logsfile')
# 设置输出报告文件夹路径
REPORTS = os.path.join(BASE_PATH, 'Outputs/reports')
# 设置输出截图文件夹路径
SCREEN_PATH = os.path.join(BASE_PATH, 'Outputs/pageshots')
# 获取配置文件路径
YAML_PATH = os.path.join(BASE_PATH, 'Commons/testcase.yaml')

