#  input 函数会等待用户输入
username = input("请输入用户名:")
print(type(username))  # 使用 input 函数返回的类型都为 str
password = input("请输入密码:")
print(type(password))
print("用户名为:" + username + ",密码为:" + password)