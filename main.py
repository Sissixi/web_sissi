"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 8:41
"""
import pytest
import time

if __name__ == '__main__':
    report_name = time.strftime("%Y-%m-%d %H-%M-%S") + '_' + "result.html"
    pytest.main(["-m","process",
                 "--reruns", "2", "--reruns-delay", "3",
                 "--html=Outputs/reports/" + report_name,
                 "--alluredir=Outputs/allure_reports"])
