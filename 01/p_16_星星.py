"""
打印小星星
"""
num = 1
while num <= 5:
    print("*" * num)  # 使用Python运算符的特性
    num += 1

print("---------分-----割-----线----------")

# 使用原始方式
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")  # print 函数默认会换行，如果不想换行，可指定 end 参数为 ""
        col += 1
    print("")  # 换行打印
    row += 1
