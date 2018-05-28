"""
except 可以有多个

"""

try:
    result = int(input("请输入数字:"))
    print(10 / result)
except ValueError:
    print("你输入的不是数字...")
except ZeroDivisionError:
    print("输入的数字不能是0")
