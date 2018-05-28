"""
    当使用 类名() 创建对象时,Python 会执行以下操作:
        1. 为对象在内存中分配空间
        2. 为对象的属性设置初始化方法 __init__

"""


class Cat:

    def __init__(self):
        """
        __init__ 方法是专门用来定义类具有哪些属性的方法
        """
        print("这是一个初始化方法,每创建一个对象的实例都会执行一次...")

        self.name = "Tom"  # 定义Cat 类的 name属性

    def eat(self):
        print("%s 爱吃鱼" % self.name)  # 在 __init__ 方法中定义了name ,在这个方法中就可以通过 self来获取对应的属性


# 创建对象
tom = Cat()
print(tom.name)
tom.eat()
