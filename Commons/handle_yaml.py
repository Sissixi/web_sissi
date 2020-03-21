"""
-*-coding:utf-8 -*-
Author:xixi
Time:2020/2/20 0020 下午 8:37
"""
import yaml
import os
from Commons.handle_Path import YAML_PATH


class HandleYaml:
    '''读取yaml文件'''

    def __init__(self, filename):
        with open(filename, encoding="utf8")as one_file:
            # self.datas内的数据是嵌套字典的字典
            self.datas = yaml.full_load(one_file)

    def read_yaml(self, section, option):
        return self.datas[section][option]

    '''写入yamL文件的方法'''

    @staticmethod
    def write_yaml(data, filename):
        '''
        写入文件的方法
        :param data:写入嵌套字典的字典
        :param filename:写入的文件名
        :return:
        '''
        with open(filename, "w", encoding="utf8")as two_file:
            yaml.dump(data, two_file, allow_unicode=True)


do_yaml = HandleYaml(YAML_PATH)

if __name__ == '__main__':
    do_yaml = HandleYaml(YAML_PATH)
    print(do_yaml.read_yaml("logsfile", "logsname"))