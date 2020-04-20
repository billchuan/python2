# # 4月20日学习
# # 异常捕获完整语法
# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except 错误类型2:
#     # 针对错误类型2，对应的代码处理
#     pass
# except （错误类型3, 错误类型4):
# # 针对错误类型3和4，对应的代码处理
#     pass
# except Exception as result:
#     # 打印错误信息
#     print(result)
# else:
#     # 没有异常才会执行的代码
#     pass
# finally:
#     # 无论是否有异常，都会执行的代码
#     print("无论是否有异常，都会执行的代码")

# 习题1
# try:
#     tup_1 = (1, 2, 3)
#     tup_1[1] = 6
#     print(tup_1)
# except TypeError:
#     print("类型错误，元组中的元素不支持修改")

# try:
#     s1 = "zhangsan"
#     s2 = int(s1)
# except ValueError:
#     print("类型转换错误")
#
# print("其他代码")

# 简单的异常捕获
# try:
#     age_str = input("请输入年龄:")
#     age = int(age_str)
#     print(age)
# except ValueError:
#     print("请输入整数")
#
# print("其他代码")

# 异常类型捕获

# try:
#     num_str = input("请输入数据:")
#     num = int(num_str)  # ValueError
#     n2 = 10 / num  # ZeroDivisionError
#     # s2 = "www" + n2
# except ValueError:
#     print("请输入整数")
# except ZeroDivisionError:
#     print("除数不能为零")
# except Exception as message:
#     print("未知错误%s" % message)
# else:  # 没有异常
#     print("执行else语句")
# finally:  # 无论是否有都会执行
#     print("执行finally语句")
# print("其他功能代码")


# 代码的传递性
def demo1():
    return int(input("请输入整数:"))


def demo2():
    return demo1()


n = demo2()
print(n)

print("其他功能代码")
