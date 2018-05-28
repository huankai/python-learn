"""
使用 for 遍历
"""
person = {"name": "小明", "age": 20, "height": 1.78}
for key in person:
    print("key : %s ,value %s" % (key, person.get(key)))
    print(type(person.get(key)))
