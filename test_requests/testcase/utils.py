"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from jsonpath import jsonpath
from ruamel import yaml


class Utils:

    @classmethod
    def get_yaml_data(cls, file_path):
        '''
        封装 yaml 文件读取方法
        :param file_path: yaml 文件路径
        :return: yaml 文件的内容
        '''
        with open(file_path) as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls, obj, json_expr):
        '''
        封装 jsonpath 断言
        :param obj: 要断言的响应的内容
        :param json_expr: jsonpath 表达式
        :return: 提取的列表
        '''
        return jsonpath(obj, json_expr)