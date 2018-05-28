"""
    上面的例子(p_05_对象初始化)中,在 __init__方法中将 name的属性固定了,在开发中一般不这样做,
    如果想要在对象初始化时设置属性值,可以在__init__ 方法的 self 参数后加自定义的参数,
    在创建这个对象的实例时,可以加入对应的参数,如下

"""


class Cat:

    def __init__(self, name):
        """
         __init__ 方法添加接收外部传的参数 name
        """
        self.name = name  # 将传过来的name属性赋值给 Cat 类的name 属性

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 创建对象,并传入一个参数
tom = Cat("Tom")
print(tom.name)
tom.eat()

tom_2 = Cat("Tom_2")
print(tom_2.name)
tom_2.eat()
