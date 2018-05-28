"""
    函数的返回值:
        如果函数有返回值，直接使用 return 将值返回即可，如 #sum_num函数
        如果函数的返回值为元组，可以省略小括号，查看 demo2()方法

"""


def sum_num(args1, args2):
    """
    计算两个参数的加法，将结果返回
    :param args1:
    :param args2:
    :return:
    """
    return args1 + args2


result = sum_num(1, 2)
print("result = %d" % result)

print("-------分---割---线----------")


def demo2():
    """
    返回元组，小括号可以省略，pycharm会给出下划线提示
    :return:
    """
    # return (1, 2)
    return 1, 2


result = demo2()
print(result)

# 如果函数返回的是元组，可以使用多个变量来接受返回的结果，
# 变量个数必须与返回的元组元素个数相同
result_1, result_2 = demo2()  # demo2函数返回元组个数为2 ，使用两个变量来依次接收
print(result_1)
print(result_2)
