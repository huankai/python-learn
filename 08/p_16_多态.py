"""
 多态
"""


class Person(object):

    def __init__(self, name):
        self.name = name

    def work(self):
        """
        工作
        """
        pass


class Programmer(Person):
    """
    程序员
    """

    def work(self):
        print("程序员: %s 在写代码..." % self.name)


class Sale(Person):
    """
    销售员
    """

    def work(self):
        print("销售员: %s 在陪客户..." % self.name)


class Boss(object):

    def plan_task(self, persion):
        """
            老板指挥人工作，使用多态
        :param persion:
        """
        persion.work()


# 注意，Programmer 继承了 Person,Person 的__init__方法中需要参数 name，子类也需要传入，除非重写了子类的_init__ 方法
programmer = Programmer("小明")

sale = Sale("小芳")

gl_boss = Boss()
gl_boss.plan_task(programmer)
gl_boss.plan_task(sale)
