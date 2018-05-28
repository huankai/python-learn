"""
类方法定义 ：
    需要在方法名上加 @classmethod修饰
    并且方法的第一个参数必须为　cls ， 可以通过 cls 来调用其它类方法或类属性
"""


class Tool(object):
    num = 10

    @classmethod
    def demo(cls):
        print("类方法demo")

    @classmethod
    def demo2(cls):
        cls.demo()
        print("类方法获取类属性: %d" % cls.num)
        print("类方法demo2")


Tool.demo()
Tool.demo2()
