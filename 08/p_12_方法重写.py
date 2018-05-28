"""
子类重写父类方法,
    如果父类的方法不能满足子类的方法
    只需要在子类中定义与父类相同名的方法即可
"""


class Animal:

    def eat(self):
        print("吃...")

    def sleep(self):
        print("睡...")

    def run(self):
        print("跑...")


class Dog(Animal):
    """
    Dog  继承于 Animal ，有 Animal的所有属性和方法
    """

    def sleep(self):
        super().sleep()
        # 如果还需要调用父类方法，可以使用 super().父类方法名 来调用父类方法
        # super() 在 Python中是一个特殊的类

        # 在Python2 版本中，以 父类名.方法名(self) 来调用父类方法，以self做为参数传入，但在python3中，不建议使用此种方式，而使用 super()
        # Animal.sleep(self)

        print("狗在睡...")

    def bark(self):
        print("叫...")

    def test(self):
        self.run()  # 子类可以调用父类的公有方法与公有属性,但不能调用父类的私有属性与私有方法


dog = Dog()
dog.sleep()  # 子类重写了此方法，会调用子类方法

dog.test()
