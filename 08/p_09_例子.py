"""
一个类可以是另一个类的属性
    枪是士兵的一个属性
"""


class Gun:
    """
    枪
    """

    def __init__(self, model, bullet_count=10):
        """

        :param model: 枪型号
        :param bullet_count: 子弹数，默认为10
        """
        self.model = model
        self.bullet_count = bullet_count  # 子弹数量

    def add_bullet(self, bullet_num):
        """
        添加子弹
        :param bullet_num:子弹数
        """
        self.bullet_count += bullet_num

    def shoot(self):
        """
            发射子弹
        """
        if self.bullet_count > 0:
            print("%s 发射子弹..." % self.model)
            self.bullet_count -= 1
        else:
            print("没有子弹了....")

    def __str__(self):
        return "model :%s,bullet_count: %d" % (self.model, self.bullet_count)


ak47 = Gun("AK47")


# ak47.add_bullet(10)
# ak47.shoot()


class Soldier:
    """
    士兵
    """

    def __init__(self, name):
        self.name = name
        self.gun = None  # None 可以用于任意类型，不表示任何值，相当于Java中的 null

    def fire(self):
        """
        士兵开枪
        """
        gun = self.gun
        if gun is None:
            """
                身份运算符：
                    is None ：判断两个标识符是否引用同一个对象,如 x is y ，类似于 id(x) == id(y)
                    is not None ：与 is None 相反
                
                is None 与 == 区别：
                    is None 比较的是内存地址
                    == 比较的是两个变量的值是否相等
                    
                    如果在判断对象时，建议使用 is None 或 is not None 
            """
            print("%s 还没有枪，无法开枪...")
        else:
            if gun.bullet_count == 0:
                gun.add_bullet(10)
            gun.shoot()
        print(self)

    def __str__(self):
        return "name :%s ,gun: %s" % (self.name, self.gun)


gl_xusanduo = Soldier("许三多")
gl_xusanduo.gun = ak47

print(gl_xusanduo)
gl_xusanduo.fire()
