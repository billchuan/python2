# 3月24日第十五次课上课代码

# 全局变量修改
# name = "zhangsan"
#
#
# def method_1():
#     global name
#     name = "lisi"
#     print(name)
#
#
# method_1()
# print(name)


# 函数嵌套
# 在method_1中调用method_2
# def method_2():
#     print("2" * 50)
#
#
# def method_1():
#     print("1" * 50)
#     method_2()
#     print("1" * 50)
#
#
# method_1()


# 函数递归
def print_num(num):
    if num == 4:
        return
    print(num)
    print_num(num + 1)
    print(num)


print_num(1)
