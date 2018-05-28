"""
有时候，函数接收的参数个数是不确定的，就可以使用多值参数
    python中有两种多值参数：
        参数名前加一个 * 可以接收元组
        参数名前加两个 * 可以接收字典

    一般在给多值参数命名时，习惯使用以下两个名字
        *args 存放元组参数，arguments 缩写
        **kwargs    存放字典参数， keyword arguments 缩写

"""


def demo(num, *args, **kwargs):
    """

    :param num:
    :param args:
    :param kwargs:
    :return:
    """
    print(num)
    print(args)
    print(kwargs)


# demo(1, 2, 3, 4, 5)  # 1被 num 接收 ，(2,3,4,5)都被args接收
demo(1, 2, 3, name="小明", age=10)  # 1被 num 接收 ，(2,3)被args接收 ，{name="小明", age=10}被kwargs接收
