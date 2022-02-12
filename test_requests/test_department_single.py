"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest
import requests


class TestDepartmentSingle:
    '''
    单接口验证
    '''

    def setup_class(self):
        # 定义凭证
        corpid = "ww876064acebf0fa3c"
        corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        # 定义 params
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 调用底层的 request 方法，支持不同的请求方式
        r = requests.request(method="GET", url=url, params=params)
        # 打印响应
        print(r.json())
        # 获取 access_token
        self.token = r.json()["access_token"]

    @pytest.mark.parametrize(
        "name, name_en, parentid, order, depart_id, expect",
        [
            ("技术部", "JISHU1", 1, 1, 2, 0),
            ("", "JISHU2", 1, 2, 3, 40058),
            ("j", "JISHU3", 1, 3, 4, 0)
        ]
    )
    def test_create_department(self, name, name_en, parentid, order, depart_id, expect):
        '''
        创建部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"

        data = {
            "name": name,
            "name_en": name_en,
            "parentid": parentid,
            "order": order,
            "id": depart_id
        }

        # 发出 post 请求
        # 企业微信中所有接口请求和响应都是用 json 数据格式
        r = requests.request(method="POST", url=url, json=data)
        # 业务断言
        assert r.json()["errcode"] == expect