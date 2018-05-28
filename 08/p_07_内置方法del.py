"""
    内置方法 __del__
        当一个对象被从内存中销毁时,会自动调用 __del__ 方法
        如果需要在对象销毁前执行一些操作,可以定义  __del__ 方法

"""


class Car:

    def __init__(self, name):
        self.name = name
        print("name is %s" % name)

    def __del__(self):
        print("del 方法调用了")


tom = Car("tom")

del tom  # 销毁tom 实例 ,会调用 __del__ 方法

print("-" * 10)
