"""
函数参数的默认值：
    函数参数的默认值，只需要在参数后加 = 默认值即可
    如 gender = True
    注意：
        1、默认值只能定义在函数参数的最后面，可以有多个默认值，
        2、在调用函数时，如果函数参数有多个默认参数，必须使用 参数名=value 的格式，否则，参数会使用第一个默认参数
            如下定义的方法
                demo("xiaoming",10)  10会被 gender接收
                demo("xiaoming",age=10)  接收参数结果是 gender = True， age = 10
"""


def demo(name, gender=True, age=1):
    """

    :param name:  姓名
    :param gender: 性别，默认值为True
    :param age:  年龄，默认为1
    """
    sex_name = "男生"
    if not gender:
        sex_name = "女生"
    print("%s 是 %s" % (name, sex_name))
    print(gender)
    print(age)


demo("小明", age=10)
# demo("xiaoming", 10)
# demo("xiaoming", age=10)
