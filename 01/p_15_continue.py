"""
continue ：停止本次循环，继续下次循环
"""

num = 0
while num < 20:
    num += 1
    if num == 10:
        continue
    print("num= %d" % num)
