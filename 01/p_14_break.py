"""
break ：退出循环
"""

num = 0
while num < 20:
    num += 1
    if num == 15:
        break
    print("num= %d" % num)
