"""
if 语法:
    if+空格+表达式+:
        条件成立后需要执行的代码需要有tab缩进，也就是说：if语句与缩进代码块是一个完整的代码块
"""
flag = False
if flag:
    print("True")
    print("条件成立时会执行")

if not flag:  # 取反
    print("False")

print("总会执行")
