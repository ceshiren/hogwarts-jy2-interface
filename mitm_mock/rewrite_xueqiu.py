"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 使用 json loads 方法，把响应转化为 python 对象
        data = json.loads(flow.response.content)
        # 修改响应内容
        data['data']['items'][0]['quote']['name'] = "hogwarts001"
        data['data']['items'][1]['quote']['name'] = "hogwarts002"
        data['data']['items'][1]['quote']['current'] = 10000
        # 把字典转为字符串，赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
