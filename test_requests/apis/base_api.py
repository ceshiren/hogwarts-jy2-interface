"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import logging

import requests


class BaseApi:
    # 指定 log 日志的存放位置（需要先创建目录，否则会报错）
    # 指定日志的编码格式
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    # 设置日志的等级
    logging.getLogger().setLevel(0)
    # 设置日志的内容格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    # 设置生效
    logging.getLogger().addHandler(fileHandler)

    def log_info(self, msg):
        '''
        日志方法
        :param msg: 要打印到日志中的信息
        :return: info 级别的日志
        '''
        return logging.info(msg)

    def send_api(self, req):
        '''
        对 requests 尽心二次封装
        :return: 接口响应结果
        '''
        # req = {
        #     "method":"GET",
        #     "url":"xxxxx",
        #     "params":{},
        #     "json":{}
        # }
        self.log_info("--------- requests data ---------")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("--------- response data ---------")
        self.log_info(r.json())
        return r