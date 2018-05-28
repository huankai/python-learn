"""
注意:字典中的key的类型只能是不可变类型,在Python中,字典的key会使用hash方法计算key的hash值
    hash 方法接受一个参数，这个参数的类型也只能是不可变类型
"""

print(hash(1))
print(hash(1.88))
print(hash("445"))
print(hash((1,)))
# print(hash([1, 5]))  # hash 列表类型的参数，会报错
# print(hash({"name": "zs"}))  # hash 字典类型的参数，会报错
