# 多值函数中元组与字典的拆包


def demo(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    print(args)
    print(kwargs)


gl_dict = {"name": "小明", "age": 10}
gl_nums = (1, 2, 3)

# demo(gl_nums, gl_dict)  # 不使用拆包语法 ，所有参数会被 args 接收


# 使用拆包语法 ：
#     在调用函数的元组变量前加一个 * ，在调用函数的字典变量前加两个 *
demo(*gl_nums, **gl_dict)  # 使用拆包语法，gl_nums 被 args接收,gl_dice被kwargs接收
