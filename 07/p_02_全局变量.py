# 定义全局变量，因为Python程序从上到下执行，所以一般将全局变量定义到import 语句下面、函数的上面
# 如果变量定义在函数调用之后，可能会报错
# 一般会在全局变量命名时加上  g_ 或 gl_ 前缀 ，如 gl_num ，就表示一个全局变量
num = 10


def demo1():
    """
     在函数内部不能直接给全局变量赋值，而是会声明一个相同的局部变量
        如果一定要修改全局变量呢，请看 下面的demo3方法
    :return:
    """
    num = 99  # 定义局部变量，此变量名与全局变量名相同，都叫 num ，pycharm会提示此变量已在全局变量中声明，为避免混淆，会有下滑线提示
    print("num value is  %d" % num)  # 99


def demo2():
    """
        如果 num 在函数内部没有定义，会使用全局变量 num，如果还找不到，报错
    :return:
    """
    print("num value is  %d" % num)  # 10


demo1()
demo2()

print("-----分---割---线--------")


def demo3():
    """
        如果想要修改全局变量的值，可以使用 global 关键字声明变量
        然后再修改此变量的值即可

    :return:
    """
    global num
    num = 88
    print("num value is  %d" % num)  # 99


demo2()
demo3()
