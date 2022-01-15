"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from mitmproxy import http

# request 名称不可以改变
# 当 mitmdump 加载这个脚本的时候，当有请求来，就会回调 request 方法
# flow 就是 mitmdump 抓到的接口数据
def request(flow: http.HTTPFlow) -> None:
    # 修改判断条件
    if "quote.json" in flow.request.pretty_url:
        # 打开本地数据文件
        with open("/Users/mac/Desktop/quote.json") as f:
            # 创建一个响应，返回给客户端
            flow.response = http.HTTPResponse.make(
                200,  # 响应状态码
                # 读取文件中的数据作为响应内容
                f.read(),
                {"Content-Type": "application/json"}  # 通过设置头信息指定响应格式
            )