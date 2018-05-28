"""
Python中可以有多继承，这点与 Java 不同
    语法 :
        class 类名(父类1,父类2,...)

    继承后，该子类拥有所有父类的属性和方法
        如果继承的这些类中，有相同的方法，Python会根据 __mro__ (method resolution order)(方法搜索顺序) 从左到右查询的
        直到查询到了该方法，则执行，否则报错
        查看 __mro__ 可以直接使用 类名.__mro__　查看
        如下：
        Child.__mro__ 结果为 :(<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
        可知：
            如果要调用 demo 方法，会从Child -> Father -> Mother -> object 这样的顺序查询
            object 是python中所有类的父类

        不过，在开发中，应该避免这种情况，或者避免使用多继承
"""


class Father:
    def demo(self):
        print("Father Demo")


class Mother:
    def demo(self):
        print("Mother demo")

    def demo2(self):
        print("Mother demo2")


class Child(Father, Mother):
    """
    孩子继承父亲与母亲两个类
    """

    def test(self):
        super().demo()


child = Child()
child.test()
child.demo()
child.demo2()


#  mro()
print(Child.__mro__)
