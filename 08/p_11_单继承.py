"""
继承：
    只需要在子类后面加上 (要继承的类) 即可，继承后，子类就有了父类的所有属性和方法
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

    def bark(self):
        print("叫...")


dog = Dog()
dog.run()
dog.eat()
dog.bark()
dog.sleep()

print("*" * 30)


class XiaoTianQuan(Dog):

    def fly(self):
        print("哮天犬飞起来咯...")


xiao_tain_quan = XiaoTianQuan()
xiao_tain_quan.sleep()
xiao_tain_quan.eat()
xiao_tain_quan.fly()
