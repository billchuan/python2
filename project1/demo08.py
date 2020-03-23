# 3月23日学习代码

# 1、创建一个函数，计算20+30的值

# def sum_2():
#     n1 = 20
#     n2 = 30
#     sum1 = n1 + n2
#     print("%d+%d=%d" % (n1, n2, sum1))
#
#
# sum_2()


# 2、修改函数，提高该函数的通用性，使其能计算任意2个数的和

# def sum_2(n1, n2):
#     """计算任意两个数的和"""
#     result = n1 + n2
#     print("%d+%d=%d" % (n1, n2, result))
#
#
# sum_2(10, 20)


# 3、默认参数的定义与调用
# 打印班级同学的信息 姓名 年龄 国籍(中国)

# def print_stu_info(name, age, country="中国"):
#     print("该同学名字为:%s,年龄为:%d,国籍为:%s" % (name, age, country))
#
#
# print_stu_info("lisi", 17)


# 练习1
def print_info(class_num, name):
    print("欢迎%d班%s同学进入Python直播间" % (class_num, name))


print_info(21810, "张三")
