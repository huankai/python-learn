"""
列表中有很多常用的方法，用来对元素的查询、添加、修改、删除、排序、记数等操作
注意:
    列表中元素没有规定一定使用相同的类型，但如果使用了不同的类型，可能 列表中的某些方法在调用时会报错
    如 ：name_list = ["zhangsan", "lisi", "wangwu", 10] ，此列表中有str和 int 类型的元素
    此时调用  name_list.sort()时会报错
    所以，在开发中这种情况不常见
"""

name_list = ["zhangsan", "lisi", "wangwu", "zl"]
print(name_list)

print(name_list[0])  # 获取第0个元素，索引从0 开始
print(name_list[1])  # 获取第1个元素
print(name_list[2])  # 获取第2个元素
print(name_list[3])  # 获取第3个元素
# print(name_list[4])  # 获取第4个元素，报错


# 1、查询:
# 　查询指定元素第一次出现的索引，如果查询一个不存在的元素，会报错
print(name_list.index("zl"))

# 2、添加:
# append 会添加到最后
# name_list.append("zaoliu")

# insert会添加元素到指定的索引
# name_list.insert(0, "insert")

# extend 会添加到最后
# name_list.extend(["a", "b", "a"])

# 3、修改：
# 直接指定索引值修改
# name_list[0] = "a"

# 4、删除：
# 删除元素第一次出现,如果元素不存在，会报错
# name_list.remove("a")
# 删除还可以使用 del 关键字删除
# del name_list[0]

# 5、记数：
# 记录元素出现的个数
print(name_list.count("a"))

# 6、获取 name_list的长度
print("name_list长度为: %d" % len(name_list))

# 7、数据反转
name_list.reverse()

# 8、排序
#  如果要降序，可以设置reverse 参数为True， 默认为 False
# name_list.sort()
# name_list.sort(reverse=True)

print(name_list)
