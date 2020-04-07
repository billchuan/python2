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
name_list1 = ["zs", "ls", 12, "zs"]
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
name_list2 = [1, 2, 3, 4]
name_list1.extend(name_list2)
print(name_list1)
