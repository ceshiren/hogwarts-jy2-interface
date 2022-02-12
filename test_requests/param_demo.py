"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

def param_demo(a, b, c):
    print(f"a={a}, b={b}, c={c}")

if __name__ == '__main__':
    # 位置参数
    param_demo(1, 2, 3)
    # 关键字参数
    param_demo(b=2, a=1, c=3)

    # 定义结构体
    data = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    # 解包，**data 字典解包之后，通过关键字传参的方式给函数传递参数
    # 等通过 param_demo(b=2, a=1, c=3)
    param_demo(**data)