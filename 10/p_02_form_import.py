from p_01_module1 import demo1 as module1_demo1
from p_01_module2 import demo1

# 使用 from 导入demo1后，不需要再用 p_01_module1.demo1()再调用，直接 demo1()即可
# 导入的两个模块中都有 demo1方法，会使用后导入的方法
demo1()

# 使用别名的方式
module1_demo1()
