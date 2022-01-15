"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 拿到响应的时候调用 response 方法
# flow 代表响应数据
from mitmproxy import http


def response(flow: http.HTTPFlow):
    print(flow.response.content)