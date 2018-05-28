"""
让类创建的对象，在系统中只存在一个实例，
每次执行 类名() 返回的对象都是相同的实例

    使用 类名() 创建对象时， Python 解析器首先会调用内置的父类 __new__ 方法为对象分配空间
        __new__ 方法是 object 提供的内置静态方法，主要作用有两个：
            1.在内存中为对象分配空间
            2.返回对象的引用
        python解析器获得对象的引用后，将此引用做为第一个参数传递给 __init__ 的第一个参数
        重写 __new__ 方法一定要非常固定，要有返回值 : return super().__new__(cls)
        否则 ，python 解析器得不到分配了空间的对象引用，就不会调用对象的 __init__ 方法
        __new__ 方法是一个静态方法，在调用时需要主动传递 cls 参数


"""


class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
        # print("执行 new 方法...")
        # return super().__new__(cls)

    def __init__(self):
        print("初始化...")


gl_player = MusicPlayer()
gl_player2 = MusicPlayer()

print(gl_player is gl_player2)  # True
