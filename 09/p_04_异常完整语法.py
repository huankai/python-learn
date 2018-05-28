"""
    try:
        执行的代码
    except 错误类型1:
        错误捕捉
    except 错误类型2:
        错误捕捉2
    except (错误类型3,错误类型4):
        错误捕捉3和错误捕捉4
    except Exception as e:
        未知错误
    else:
        没有异常才会执行
    finally:
        无论是否有异常，都会执行

"""

try:
    result = int(input("请输入数字:"))
    print(10 / result)
except ValueError:
    print("你输入的不是数字...")
except ZeroDivisionError as e:
    print("输入的数字不能是0 ,错误信息: %s" % e)
except Exception as e:  # 只有上面定义的错误类型不存在时，有错误的情况下才会进入到此except中
    print("未知错误:错误信息: %s" % e)
else:
    print("没有错误，才执行")
finally:
    print("无论是否有异常，都会执行")
