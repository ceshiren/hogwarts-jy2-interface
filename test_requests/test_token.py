"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests


class TestToken:

    def test_get_token(self):
        '''
        获取 access_token
        '''
        # 定义凭证
        corpid = "ww876064acebf0fa3c"
        corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

        # 发 get 请求
        r = requests.get(url)

        # 打印响应
        print(r.json())


    def test_get_token2(self):
        '''
        获取 token 的第二种方法
        '''
        # 定义凭证
        corpid = "ww876064acebf0fa3c"
        corpsecret = "A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9YxY"

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"

        # 定义 params
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发 get 请求
        # r = requests.get(url, params)
        # 调用底层的 request 方法，支持不同的请求方式
        r = requests.request(method="GET", url=url, params=params)
        # 打印响应
        print(r.json())

