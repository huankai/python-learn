def input_password():
    password = input("请输入密码:")
    if len(password) < 8:
        raise Exception("密码长度不够,长度为: %d" % len(password))
    return password


print(input_password())
