"""
在Python 中: str、int、float、bool、元组(tuple) 是不可变类型，
                因为这些类型的变量一旦定义，不可再改变，
                如果是重新附值，则此变量的内存引用不再是原来的引用
              列表、字典是可变类型
                列表与字典类型可以通过对应的方法来列表或字典中的元素进行增加、删除、修改操作
                并不会将变量的内存引用修改。

            对象的引用地址，可以通过 id(变量名) 方法来调用
"""

name = "zhangsan"
print("name 的 id值为: %d" % id(name))

age = 18
print("age 的 id值为: %d" % id(age))

price = 1.76
print("price 的 id值为: %d" % id(price))

tuple_1 = (1,)
print("tuple_1 的 id值为: %d" % id(tuple_1))

list_1 = [1, 6]
print("list_1 的 id值为: %d" % id(list_1))
list_1.append(58)
print("list_1 的 id值为: %d" % id(list_1))  # 列表 list_1 添加元素后不会改变id值

dict_1 = {"age": 18, "name": "zs"}
print("dict_1 的 id值为: %d" % id(dict_1))
dict_1["sex"] = "男"
print("dict_1 的 id值为: %d" % id(dict_1))  # 字典dict_1 添加元素后不会改变id值


