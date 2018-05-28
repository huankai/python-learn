"""
元组与 列表的转换
"""

tuple_1 = ("zs", 3.14, 5)

# list 函数，将 元组转换为 list
list_1 = list(tuple_1)
print(type(list_1))

# tuple 函数，将 list 转换为 tuple
tuple_2 = tuple(list_1)
print(type(tuple_2))