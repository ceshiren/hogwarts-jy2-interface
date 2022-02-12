"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

from test_requests.apis.wework import WeWork
from test_requests.testcase.utils import Utils

'''
接口信息描述：只关注接口本身，不需要做断言

每个方法要返回接口的响应内容
'''

class Department(WeWork):

    def create_department(self, data):
        '''
        创建部门
        :return: 创建部门接口响应
        '''
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        req = {
            "method": "POST",
            "url": create_url,
            "json": data
        }
        # r = requests.request(method="POST", url=create_url, json=data)
        r = self.send_api(req)
        return r.json()

    def update_department(self, data):
        '''
        更新部门信息
        :return: 更新部门接口响应
        '''
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        req = {
            "method": "POST",
            "url": update_url,
            "json": data
        }
        # r = requests.request(method="POST", url=update_url, json=data)
        r = self.send_api(req)
        return r.json()

    def delete_department(self, depart_id):
        '''
        删除部门信息
        :return: 删除部门接口响应
        '''
        deletle_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={depart_id}"
        req = {
            "method": "GET",
            "url": deletle_url
        }
        # r = requests.request(method="GET", url=deletle_url)
        r = self.send_api(req)
        return r.json()

    def get_departments(self):
        '''
        获取部门信息
        :return: 获取部门信息接口响应
        '''
        get_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "GET",
            "url": get_url
        }
        # r = requests.request(method="GET", url=get_url)
        r = self.send_api(req)
        return r.json()

    def clear_departments(self):
        '''
        清理已经存在的部门信息
        :return:
        '''
        # 查询目前存在的部门
        depart_list = self.get_departments()
        # 提取部门 id 列表
        id_list = Utils.base_jsonpath(depart_list, "$..id")
        # id 为 1 的是基础的父部门，不能删除
        for i in id_list:
            if i != 1:
                # 调用删除部门接口清除所有部门数据
                self.delete_department(i)