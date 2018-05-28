"""
  object类是 Python 中所有类的父类，提供了一些内置属性和方法，可以使用 dir函数查看
  新式类：
    以object 类为父类的类，推荐使用
  旧式类(经典类):
    不以 object 为父类的类，不推荐使用

  在python3中定义类时，如果没有指定父类，则默认会以 object 作为该类的父类，python3中定义的类都是新式类
  在 Python2.x中定义类时，如果没有指定交类，不会以 object 作为该 类的父类，

  新式类和经典类在多继承时，会影响到方法的搜索顺序(__mro__)

  为保证写代码能同时在python2与python3中运行，
    在定义类时，如果没有父类，建议都继承 object
     如: class 类名(object)
"""