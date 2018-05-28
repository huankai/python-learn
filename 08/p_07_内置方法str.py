"""
    内置方法 __str__
        默认情况下,使用print() 直接打印一个对象时,会答应该对象的内存地址,
        如果不想打印内存存在,可以定义内置的 __str__ 方法,
        就相当于Java中的toString方法.
        __str__ 方法,必须有返回值,返回值类型为 str
"""


class Car:

    def __init__(self, name):
        self.name = name
        print("name is %s" % name)

    def __str__(self):
        """
        str 方法,必须有返回值,返回值类型为 str
        :return:
        """
        return self.name


tom = Car("tom")
print(tom)
