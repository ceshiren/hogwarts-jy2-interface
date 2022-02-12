"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests


class TestWework:

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
        # 定义操作的部门 id
        self.depart_id = 3

    def test_create_department(self):
        '''
        创建部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"

        data = {
            "name": "hogwarts111",
            "name_en": "h111",
            "parentid": 1,
            "order": 2,
            "id": self.depart_id
        }

        # 发出 post 请求
        # 企业微信中所有接口请求和响应都是用 json 数据格式
        r = requests.request(method="POST", url=url, json=data)
        # 业务断言
        assert r.json()["errcode"] == 0
        # 通过查询部门列表接口的返回值，验证部门是否创建成功
        depart_info = self.test_get_departments()
        print(depart_info)
        assert depart_info["department"][1]["name"] == "hogwarts111"

    def test_update_department(self):
        '''
        更新部门信息
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"

        data = {
            "id": self.depart_id,
            "name": "hogwarts111-update"
        }

        r = requests.request(method="POST", url=url, json=data)

        assert r.json()["errcode"] == 0
        depart_info = self.test_get_departments()
        assert depart_info["department"][1]["name"] == "hogwarts111-update"


    def test_delete_department(self):
        '''
        删除部门
        :return:
        '''
        # 指定删除部门的id
        # id = 3
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={self.depart_id}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errcode"] == 0
        depart_info = self.test_get_departments()
        assert len(depart_info["department"]) == 1

    def test_get_departments(self):
        '''
        获取当前已经存在的所有的部门信息
        :return: r.json() 查询到的所有的部门信息
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        print(r.json())
        assert r.json()["errcode"] == 0
        return r.json()
