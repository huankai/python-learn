"""
    新房添加家具，每添加家具前，判断房间面积是否能容下家具所占用的面积 ：
        如果容不下，不能添加家具
        如果容得下，添加家具后，再将空闲面积减少家具占用的面积
"""


class HouseItem:
    """
    家具
    """

    def __init__(self, name, area):
        """

        :param name: 家具名称
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "name : %s ,area : %.2f" % (self.name, self.area)


# 创建家具实例
bed = HouseItem("红木床", 4)
sofa = HouseItem("红木沙发", 15)
table = HouseItem("红木桌子", 2)


class House:
    """
    家
    """

    def __init__(self, name, area):
        """

        :param name: 户主
        :param area:  面积
        """
        self.name = name
        self.area = area
        self.rest_area = area  # 剩余面积
        self.home_item = []  # 家具列表

    def add_home_item(self, home_item):
        """
         添加家具，每添加家具，房子面积也应该减少
        :param home_item: 家具
        :return:
        """
        if home_item.area > self.rest_area:
            print("家的空闲面积不够，不能添加家具了...")
        else:
            self.rest_area -= home_item.area
        print("户主: %s ,添加家具 [%s] ，,总面积 : %.2f[剩余面积 ： %.2f]" % (self.name, home_item, self.area, self.rest_area))

    def __str__(self):
        # 对于一行比较长的，可以使用小括号包起来，然后在需要换行的位置回车即可，PyCharm会自动缩进
        return ("户主: %s ,总面积 : %.2f[剩余面积 ： %.2f]，家具: %s"
                % (self.name, self.area, self.rest_area, self.home_item))


# 创建房子，并添加家具
gl_my_house = House("Mine", 120)
gl_my_house.add_home_item(bed)
gl_my_house.add_home_item(sofa)
gl_my_house.add_home_item(table)
