"""
对象中定义的函数第一个参数必须为 self, 在写完方法名后,输入方法后面的小括号后 PyCharm会自动补齐self 参数
"""


class Cat:
    """
     定义猫对象
    """

    def eat(self):
        """
         self 表示:哪个对象的引用调用了此方法,self就这这个对象的引用
        :return:
        """
        print("%s 吃东西" % self.name)  # 如果这个对象没有name属性,会报错,对象有哪些属性,应该封装在类的内部

    def drink(self):
        """
        :return:
        """
        print("%s 喝水" % self.name)


tom = Cat()
tom.name = "Tom"  # 简单，粗暴的添加属性name

print(tom.name)
tom.eat()
tom.drink()

lazy_cat = Cat()
lazy_cat.name = "懒猫"
lazy_cat.eat()
lazy_cat.drink()
