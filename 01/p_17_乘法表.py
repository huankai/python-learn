"""
打印乘法表
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
