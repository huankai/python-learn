"""
if 表达式:

else
"""

flag = False
if flag:
    print("True")
    print("条件成立时会执行")
else:
    print("False")
print("总会执行")


# #####################################
"""
if 表达式:

elif 表达式:
 
elif 表达式:

...
 
else
"""
age = 10
if age <= 0:
    print("age不能小于等于0")
elif age < 10:
    print("age小于10")
elif age < 100:
    print("age 小于100")
else:
    print("age大于100")
