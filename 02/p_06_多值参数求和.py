def sum(*args):
    """
    
    :param args:
    :return:
    """
    result = 0
    for item in args:
        result += item
    return result


print(sum(1, 3, 5, 7, 9))
