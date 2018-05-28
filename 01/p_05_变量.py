"""
变量的命名规则:
    1、全部小写，如有多个单词，每个单词前面加 _
    2、不要使用Python 内置的关键字
"""

qq = "12345"  # 定义变量
password = '123'
print(qq)
print(password)

# ##############################################
# type 方法可返回变量的类型
qq_type = type(qq)
print(qq_type)

password_type = type(password)
print(password_type)

# ##############################################
print(2 ** 64)
# 在 pyhton 2 中，整数类型有int 和 long两种，在 python3 中，只有 int
print(type(2 ** 64))


# ##############################################
i = 10  # int 类型
f = 10.5  # float 类型
b = True  # bool 类型
print(i + f)
print(i + f + b)  # 在python 中，bool 类型可以和 int、float计算，True 的值为1 ,False 的值 为 0

# ##############################################
first_name = "张"
last_name = "三"
name = first_name + last_name  # 字符串相加结果会将字符串相连接
print(name)

# last_name = 1
# print(first_name + last_name) # 字符串不能和整数相加，会报错
