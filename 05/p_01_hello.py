person = {"name": "小明", "age": 20, "height": 1.78}
print(person)

print(person.keys())  # 获取所有的key

print(person.values())  # 获取所有的value

print(person.items())

print(person.get("name"))  # 获取指定key 的value,如果不存在，返回 None
# print(person["name"])  # 获取指定key 的value,如果不存在，报错

person["sex"] = "男"  # 如果key存在，会覆盖,否则，会新增

print(person.pop("name"))  # 弹出指定的key，并从字典中删除,key不存在，报错
# del person["name"]  # 删除,key 不存在，报错

print(len(person))  # 获取长度

temp_persion = {"email": "188@xx.com"}
person.update(temp_persion)  # 将 temp_persion 合并到 persion中，如果 temp_persion中有persion中的key,会覆盖原有的key

# 清空字典
# person.clear()

print(person)
