"""
Exception 可以捕获未知的异常

"""

try:
    result = int(input("请输入数字:"))
    print(10 / result)
except Exception as e:
    print("你输入的不是数字...,错误信息 %s" % e)
