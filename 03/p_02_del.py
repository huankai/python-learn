"""
del 关键字
 del 关键字是 delete的简写，可用来删除内存中的变量，使用del删除变量后，不能再使用删除的变量
"""

names = ["a", "b"]
del names
print(names)  # 会报错
