"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http

# request 名称不可以改变
# 当 mitmdump 加载这个脚本的时候，当有请求来，就会回调 request 方法
# flow 就是 mitmdump 抓到的接口数据
def request(flow: http.HTTPFlow) -> None:
    # 判断抓到的接口的 url 是不是我们想要修改的
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创建一个响应，返回给客户端
        flow.response = http.HTTPResponse.make(
            200,  # 响应状态码
            b"Hello World",  # 响应内容
            {"Content-Type": "text/html"}  # 通过设置头信息指定响应格式
        )