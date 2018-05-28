# 定义对象使用 class 关键字 ，类名使用大驼峰命名法(每个单词首字母大小)
#  对象中定义方法与之前的函数一样，只是在对象中定义的方法第一个参数一定是 self，
#  self 表示:哪个对象调用了此方法,self就是这个对象的引用
#  创建对象: 变量名 = 对象名() ，如  tom = Cat()
#   就可以使用对象变量名调用对象方法了


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


tom = Cat()  # 创建对象
tom.drink()  # 调用方法
tom.eat()  # 调用方法

# ---------------------------------------
#  tom 与 lazy_cat 是两个不同的对象
lazy_cat = Cat()
print(tom == lazy_cat)  # False
lazy_cat2 = lazy_cat
print(lazy_cat == lazy_cat2)  # True
