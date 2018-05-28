# 函数的递归，就是函数内部调用本身


def print_num(num):
    print(num)
    if num == 0:  # 函数跳出的条件，如果没有，会出现死循环
        return
    print_num(num - 1)  # 递归


print_num(10)

print("-----分---割---线---------")


def recursion_sum(num):
    """
    递归求和
    :param num:
    :return:
    """
    if num == 1:
        return num
    temp = recursion_sum(num - 1)
    return num + temp


print(recursion_sum(100))
