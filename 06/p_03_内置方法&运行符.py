"""
Python 中的内置方法：
    max:
    min:
    len:
    cmp: 比较，这个方法在 Python 3.x中已删除
"""

print("最大值 : %d" % max(5, 30))
print("最大值 : %s" % max("a", "b"))
print("最大值 : %s" % max([3, 10, 6], [3, 5, 6]))  # 如果比较列表，会将比较的列表中的每个元素依次比较

print("最小值 : %d" % min(5, 30))
print("最小值 : %s" % min("a", "b"))
print("最小值 : %s" % min([3, 10, 6], [3, 5, 6]))  # 如果比较列表，会将比较的列表中的每个元素依次比较

print("长度: %d" % len("name"))
# print("长度: %d" % len(4))  # int 类型不能使用len，会报错
print("长度: %d" % len([3, 10, 6]))
print("长度: %d" % len((3, 10, 6)))

"""
    运行符:
    +   ：合并，可用于字符串相连接、列表、元组合并
    in ：可用作遍历， 也可用于判断元素是否存在遍历的数据中，in 在对字典类型操作时，操作的是字典的key
    not in ： 判断元素是否不在遍历的数据中
"""
print([4, 5, 6] + [12, 3, 7])  # 列表追加,和 extend 方法效果一样
print((4, 5, 6) + (12, 3, 7))  # 元组追加
# print({"name": "zs", "age": 20} + {"sex": "男"})  # 字典不可追加，会报错，因为字典必须保证Key的唯一，使用 追加无法保证

print("----分---割---符-----")

ids = [1, 2, 3, 4, 5, 6, 7]
find_id = 4
if find_id in ids:  # 判断是否存在于列表中
    print("元素 %d 存在于列表中" % find_id)

if find_id not in ids:  # 判断是否不存在于列表中
    print("元素 %d 不存在于列表中" % find_id)

print("----分---割---符-----")
# in用于字典中
dict_list = [{"name": "zs", "age": 20, "sex": "男"}, {"sex": "男"}]
dict_key = "name"
for item in dict_list:
    if dict_key in item:
        print("key: %s,value : %s" % (dict_key, item[dict_key]))
    else:
        print("不存在key: %s" % dict_key)
