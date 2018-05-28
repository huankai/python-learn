"""
 元组(tuple)：
    注意:如果元组中只有一个元素时，此变量类型为第一个元素的类型，
        如果要将其定义为元组类型，需要在第一个元素后加 ,
        如:
        tuple_names = (5)  # 此变量  tuple_names 类型为 int
        tuple_names = ("zhangsan")  # 此变量  tuple_names 类型为 str
        tuple_names = ("zhangsan",)  # 此变量  tuple_names 类型为 tuple
"""
# 定义一个空元组
tuple_empty = ()

#
tuple_1 = ("zs", 3.14, 5)
print(tuple_1)

print(type(tuple_1))  # 类型

print(tuple_1[1])  # 获取第一个元素

print(len(tuple_1))  # 长度

print(tuple_1.count(5))  # 返回指定元素在元组中的个数

print(tuple_1.index("zs"))  # 返回指定元素在元组中的索引，从0开始，如果元素不存在，报错

# del tuple_1[0]  # 报错，元组不能删除

# print(tuple_1[5]) # 报错

