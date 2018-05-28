"""
eval 函数：
    可以将参数字符串当成表达式，计算出返回的结果,

    eval 函数很强大，使用也是非常危险的，比较接收input输入的字符串
"""

print(eval("1+2"))
print(eval("'*' * 10"))
print(type(eval("3")))
print(type(eval("(1,4,6)")))
print(type(eval("[2,9,5]")))
print(type(eval("{'name':'zs','age':14}")))

# __import__('os') 相当于 import os
# 列出当前目录下的所有文件
print(eval("__import__('os').system('dir')"))
