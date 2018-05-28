"""
给对象添加属性
    此种方式不好之处：
        没有在对象内部定义属性，不能保证每个创建该对象的实例都有这些属性
        对象内部的一些方法也无法使用这些属性
"""


class Cat:
    """
     定义猫对象
    """

    def eat(self):
        """
         猫吃东西的方法
        :return:
        """
        print("猫吃东西")

    def drink(self):
        """
        猫喝水的方法
        :return:
        """
        print("猫喝水")


tom = Cat()
tom.name = "Tom"  # 简单，粗暴的添加属性name

print(tom.name)
