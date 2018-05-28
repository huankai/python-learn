"""
Python 解析器在导入模块时：
    会先搜索当前目录下的模块名文件，如果有就直接导入
    如果没有，再搜索Python系统目录
    在开发时，给文件起名，不要和Python 系统中的文件模块名相同

    使用 python 中每个模块中的内置属性 __file__ 可以查看模块的完整路径
"""

import random

# 如果在当前目录下也存在 ranodm.py 文件，执行下面的random.randint()方法时会先从当时目录下搜索，会报错   
print(random.randint(0, 10))
print(random.__file__)  # 查看模块完整路径
