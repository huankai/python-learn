"""
子类可以访问父类的公有属性和公有方法，不能直接访问父类的私有属性和私有方法
"""


class Animal:

    def __init__(self):
        self.num1 = 10
        self.__num2 = 20  # 私有属性

    def test_print(self):
        print("公有方法")

    def __test_print(self):
        print("私有方法")


class Dog(Animal):
    """
    Dog  继承于 Animal ，有 Animal的所有属性和方法
    """

    def test(self):
        self.test_print()  # 子类可以调用父类的公有方法与公有属性,但不能调用父类的私有属性与私有方法
        print(self.num1)

        # print(self.__num2)  # 不能访问
        # self.__test_print()  # 不能访问


dog = Dog()
dog.test()  # 子类重写了此方法，会调用子类方法
