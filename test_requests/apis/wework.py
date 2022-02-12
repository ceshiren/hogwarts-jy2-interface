"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import requests

'''
企业微信特有的逻辑，完成 access_token 的获取
'''

class WeWork:

    def __init__(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        '''
        获取  access_token
        :return: access_token 值
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

        # 调用底层的 request 方法，支持不同的请求方式
        r = requests.request(method="GET", url=url, params=params)
        # 获取 access_token
        token = r.json()["access_token"]
        return token