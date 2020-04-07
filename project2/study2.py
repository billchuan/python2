# 4月7日七、八节课学习代码
# 习题1
# a = "hao,hao,xue,xi,tian,tian,xiang,shang"
# a1 = a.replace("hao,hao,xue,xi,tian,tian,xiang,shang",
#                "hao-hao-xue-xi-tian-tian-xiang-shang")
# print(a1)

# 习题2
# a = "hao-hao-xue-xi-tian-tian-xiang-shang"
# print(a.split("-"))

# 列表
# name_list1 = ["zs", "ls", 12, "zs"]
# 列表的取值
# print(name_list1[2])

# 列表的索引
# print(name_list1.index("zs"))

# 列表的修改
# name_list1[0] = "xiaoming"
# print(name_list1)

# 列表的增加
# append插入到结尾
# name_list1.append("王麻子")
# print(name_list1)
# 某个位置插入
# print(name_list1)
# name_list1.insert(3, "刘能")
# print(name_list1)
# extend将某个列表的所有数据追加到尾部
# name_list2 = [1, 2, 3, 4]
# print(name_list1)
# name_list1.extend(name_list2)
# print(name_list1)

# 列表的删除
# remove删除 如果列表中包含多个相同的元素A是，remove只会删除列表第一个
# name_list1.remove("zs")
# print(name_list1)
# clear清空列表
# print(name_list1)
# name_list1.clear()
# print(name_list1)
# pop默认删除列表中的最后一个元素 或带参删除对应索引的元素
# print(name_list1)
# name_list1.pop()
# name_list1.pop(1)
# print(name_list1)
# del 删除


# 列表的排序
# name_list1 = ["zs", "ls", "aa", "ww", "xm"]
#
# number_list1 = [3, 1, 5, 2, 7, 10, 32, 21]
# 混合排序会报错，字符串类型不能比较
# info_list = ["zs", "ls", "aa", "ww", "xm", 3, 1, 5, 2, 7, 10, 32, 21]

# sort（）升序排序
# name_list1.sort()
# print(name_list1)
#
# number_list1.sort()
# print(number_list1)
# sort()的降序排序
# name_list1.sort(reverse=True)
# print(name_list1)
#
# number_list1.sort(reverse=True)
# print(number_list1)

# 逆序
# name_list1 = ["zs", "ls", "aa", "ww", "xm"]
# number_list1 = [3, 1, 5, 2, 7, 10, 32, 21]
#
# print(name_list1)
# name_list1.reverse()
# print(name_list1)
#
# print(number_list1)
# number_list1.reverse()
# print(number_list1)


# 统计
# count
name_list = ["ls", "ls", "ls", "ls", "ww", "zs", "zs", "xm"]
i = name_list.count("ls")
print(i)

# 列表的遍历
for i1 in name_list:
    print(i1, end=" ")
