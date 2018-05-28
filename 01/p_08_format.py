name = "kally"
age = 10
print("my name is %s ,age is %d" % (name, age))

print("my name is %s" % name)  # 如果只有一个参数，后面的括号可以省略
print("my name is %%" % ())  # %% 会转义为 %
# print("my name is %% %s" % ())  # 后面的参数与前面的 format 要一致

print("my name is %06d" % age)  # %% age 长度不到 6 位，就以 0 补齐

"""
%s      字符串
%d      数字
%f      浮点类型
%.2f      浮点类型，表示小数点后保留两位小数
%%      %

"""
