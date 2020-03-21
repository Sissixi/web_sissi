"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 8:37
"""
import os
import time
import logging
from Commons.handle_yaml import do_yaml
from Commons.handle_Path import LOGS_PATH


class Mylog:
    @classmethod
    def Creatlog(cls):
        # 设置一个日志收集器
        mylog = logging.getLogger(do_yaml.read_yaml("logs", "logsname"))
        # 设置日志收集器的等级
        mylog.setLevel(do_yaml.read_yaml("logs", "logslevel"))
        # # 设置日志输出到控制台
        # sh = logging.StreamHandler()
        # # 设置日志输出控制台的格式
        # sh.setLevel(do_yaml.read_yaml("logs", "shlevel"))
        # # 日志格式设置
        formated = logging.Formatter(do_yaml.read_yaml("logs", "formated"))
        # # 将日志格式设置到输出格式
        # sh.setFormatter(formated)
        # # 将控制台输出添加到日志收集器中
        # mylog.addHandler(sh)
        # 输出到文件
        logname = do_yaml.read_yaml("logs", "fl_name")+"_" + time.strftime("%Y-%m-%d %H_%M_%S")
        fl = logging.FileHandler(filename=os.path.join(LOGS_PATH, logname),
                                 encoding="utf8")
        # 设置输出到文件的等级
        fl.setLevel(do_yaml.read_yaml("logs", "fl_leval"))
        # 设置输出到文件的格式
        fl.setFormatter(formated)
        # 输出到文件添加到收集器中
        mylog.addHandler(fl)
        return mylog


do_log = Mylog.Creatlog()
if __name__ == '__main__':
    do_log = Mylog.Creatlog()
    do_log.info("xixi")