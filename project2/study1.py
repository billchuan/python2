# 4月7日五、六节课学习代码


# java的数组
# int[]=arr={1,2,3,4,5}

# python数组

# 普通元组的创建
type_info = ("zs", 18, 1.71)
# print(type(type_info))

# 空元组
tuple_empty = ()
# print(type(tuple_empty))

# 包含一个元素的元组
tuple_one = (18)
# print(type(tuple_one))

# 取值
tuple_1 = ("张三", "李四", 123, "王五", "张三", "张三1")
# print(tuple_1[2])

# 取索引号
# print(tuple_1.index("王五"))

# 计算元组中某一元素的个数
# print(tuple_1.count("张三"))

# 习题2
# name_list = ["zs", "ls", "ww", "xl", "xz", "ls"]
# for i in name_list:
#     print(i, end=" ")

# 练习
tuple_2 = ("张三", "李四", 123, "王五", "张三", 12.3)
# for i in tuple_2:
#     print("我的名字叫", i, sep=":")

name = "zhangsan"
age = 18
tel = 11011111

# print("我的名字叫:%s,我的年龄是%d,我的电话是:%d" % (name, age, tel))

# 元组不能修改
tuple_2[0] = "lisi"
# print(tuple_2)
