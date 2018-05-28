"""
字典与列表组合使用：
"""
persion_list = [{"id": 1, "name": "zhansan", "age": 20}, {"id": 2, "name": "lisi", "age": 25}]

for item in persion_list:
    print(item)
    for item_key in item:
        print("key: %s ,value:%s" % (item_key, item.get(item_key)))
