"""
and 并，相当java中的 &&
or 或，相当Java中的 ||
not 非，相当Java中的 !

如果if 后面的表达式有多个，用and | or | not连接，并且很长，看起来不太美观，
可以将这些表达式用 () 包起来，然后在每个逻辑运算符前回车，格式如下：

if (age == 0
        or age == 1
        or age == 2
        or age == 3
        or age == 4
        or age == 5
        or age == 6):

"""

age = 10
if 0 <= age <= 120:  # 是 if age >= 0 and age <= 120 的简写
    print("合法年龄")
# if age >= 0 and age <= 120:
#     print("合法年龄")

if not 0 <= age <= 120:
    print("非法年龄")

if age >= 0 or age <= 120:
    print("合法年龄")

