"""
Python 中的私有属性与方法定义：
    只需要在属性或方法前加两个下划线 __

    私有属性与私有方法不能被外界与子类访问

    其实，在Python中，并没有严格意义上的私有属性与私有方法
        在给私有属性或私有方法命名时，实际上对名称做了一些特殊处理，使得外界无法访问
        处理方式 ：在名称前加上 _类名  => _类名__名称
        如果想在外界方法，可以使用 _类名 + 私有属性或私有方法即可访问，
        但在开发中不建议这么做

"""


class WoMen:

    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性age

    def secret(self):
        """
        非私有方法
        """
        # 在对象的方法内部，可以访问私有属性
        print("%s 年龄是 %d" % (self.name, self.__age))

    def __private_secret(self):
        """
        私有方法
        """
        # 在对象的方法内部，可以访问私有属性
        print("%s 年龄是 %d" % (self.name, self.__age))


xiaofang = WoMen("小芳")
print(xiaofang.name)  # 调用非私有属性
xiaofang.secret()  # 调用非私有方法

# print(xiaofang.__age)  # 调用私有属性,报错
# xiaofang.__private_secret()  # 调用私有方法，报错


# 使用 _类名 + 私有属性或私有方法访问
print(xiaofang._WoMen__age)
xiaofang._WoMen__private_secret()
