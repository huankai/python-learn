"""
定义函数基本语法 :
    def 函数名(形参1,形参2,...):
        函数体

注意:
    1、函数不能像 Java中有重载,如果函数名相同，会调用最下面定义的
    2、函数名要符合标识符命名规则
    3、函数不能在定义之前就调用

"""
# mult_table() 在定义之前调用会报错

"""
乘法表
"""


def mult_table():
    """
    根据 PEP8 的语法 ，定义的函数上面要保留两个空行
    打印乘法表
    函数的注释，不是放在函数名上，面是放在函数名下，这点与 Java 不同，可以按ctrl+ q 查看注释内容
    :return:
    """
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            result = row * col
            print("%d * %d = %d" % (col, row, result), end="\t")  # \t 转义字符
            col += 1
        print("")
        row += 1


def mult_table_param(max_row):
    """
    打印乘法表
    :param max_row:最大行
    :return:
    """
    row = 1
    while row <= max_row:
        col = 1
        while col <= row:
            result = row * col
            print("%d * %d\t = %d" % (col, row, result), end="\t")  # \t 转义字符
            col += 1
        print("")
        row += 1

