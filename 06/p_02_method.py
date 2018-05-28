"""
    isspace() ：判断是否为空白字符，在Python中， \t \r \n 也为空白
"""
print("".isspace())  # False
print("  ".isspace())  # True
print("\t".isspace())  # True
print("\r".isspace())  # True
print("\n".isspace())  # True
print("\t\n".isspace())  # True
print(" \t\n".isspace())  # True

print("--------分---割---符-----------")

"""
判断字符串中是否包含数字

    isdecimal: Unicode 数字、全角数字(双字节) 都返回True

    isdigit: Unicode数字、byte数字(单字节)、全角数字(双字节) 都返回True

    isnumeric: Unicode数字，全角数字（双字节），罗马数字，汉字数字 都返回True
"""
num_str = "1"
print(num_str.isdecimal())  # True
print(num_str.isdigit())  # True
print(num_str.isnumeric())  # True

# num_str = b"1"  # 转换为 byte
# print(num_str.isdecimal())   # 抛出错误
# print(num_str.isdigit())  # True
# print(num_str.isnumeric())  # 抛出错误

num_str = "Ⅳ"  # 罗马数字
print(num_str.isdecimal())  # False
print(num_str.isdigit())  # False
print(num_str.isnumeric())  # True

num_str = "三"  # 汉字
print(num_str.isdecimal())  # False
print(num_str.isdigit())  # False
print(num_str.isnumeric())  # True

print("--------分---割---符-----------")

print("所有的单词拼写首字母是否为大写，且其他字母为小写： %s" % "Username".istitle())

print("是否为小写 : %s" % "name".islower())
print("是否为大写 : %s" % "NAME".isupper())

print("是否以指定字符结束 : %s" % "NAME".endswith("ME"))  # 严格区分大小写
print("是否以指定字符开始 : %s" % "NAME".startswith("ME"))  # 严格区分大小写

print("分割 : %s" % "name1,name2".split(","))  # 严格区分大小写

print("列表join : %s" % "".join(("1", "4", "da")))  # Join
print("元组join : %s" % "".join(["1", "4", "da"]))  # Join

print("index 查询 : %d" % "name".index("m"))  # index 索引查询，查询不到会报错
print("find 查询 : %d" % "name".find("md"))  # find 索引查询，查询不到返回 -1

print("替换 查询 : %s" % "name".replace("na", "NA"))  #

print("转大写 : %s" % "name".upper())  # 转大写
print("转小写 : %s" % "NAME".lower())  # 转小写

print("左边对齐 : |%s|" % "name".ljust(10))
print("右边对齐 : |%s|" % "name".rjust(10))
print("居中对齐 : |%s|" % "name".center(10))
