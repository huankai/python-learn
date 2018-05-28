"""
使用 for 循环遍历
    for 语法 ：
        for 变量名 in  循环内容:
            # 循环方法内容
        else:
            # 当for中每个元素都遍历后才会执行，如果for中有break，并执行了 break，则else中的内容不会执行
            # else 块并不是必须的
"""

name_list = ["zhangsan", "lisi", "wangwu", "zl"]
for item in name_list:
    print("item: %s" % item)

print("-------分---割---符-------")

for item in [1, 5, 7, 3, 9]:
    print(item)
    if item == 13:
        break
else:
    print("执行了Else内容...")
