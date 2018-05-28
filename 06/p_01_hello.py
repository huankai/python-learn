username = "zhangsang"

for char in username:
    """
    字符串也可以用到遍历
    """
    print(char)

print(len(username))  # 长度

print(username.count("g"))  # 统计指定字符串出现的次数，如果不存在，返回 0

print(username.index("ang"))  # 指定字符串第一次出现的索引位置，不存在报错


