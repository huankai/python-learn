"""
使用 for 遍历元组
    在实际开发中，循环元组的情况并不多见 ，因为元组中保存的数据类型不同，
    想要对这个元组中每个不同类型的元素进行遍历，比较困难

    所以，元组类型在开发中的应用场景一般有：
        1、函数的参数或返回值
        2、格式字符串
        3、让列表不可修改，以保护数据安全
"""
tuple_1 = ("zs", 3.14, 5)
for item in tuple_1:
    print(item)
