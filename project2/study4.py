# 4月14日学习

# 习题1
# a = set(["h", "e", "l", "o"])
# print(a)

# 习题2
# s = {"zs", "ls"}
# s.update(["ww"], ["ln"], [2], [3])
# print(s)

# 字典  dictionary
# dic_1 = {"name": "zs",
#          "sex": "男",
#          "age": 18}
# print(dic_1)

# 取值
# v1=dic_1["age"]
# print(v1)

# 增加
# dic_1["height"] = 175
# print(dic_1)

# 修改
# dic_1["age"] = 19
# print(dic_1)

# 删除
# dic_1.pop("age")
# print(dic_1)

# 查看字典长度
# print(len(dic_1))

# 合并
# dic_2 = {"height": 175, "banji": 21810}
# dic_1.update(dic_2)
# print(dic_1)


# 清空
# print(dic_1)
# dic_1.clear()
# print(dic_1)

# 字典的遍历
# for i in dic_1:
#     print("%s:%s" % (i, dic_1[i]))

# 字典和列表的联合应用
# dic_1 = {"name": "zs","sex": "男","age": 18}
# dic_2 = {"name": "ls","sex": "男","age": 17}
# dic_3 = {"name": "ww","sex": "男","age": 16}

# 集合的创建(无序不重复)
# 1)
# set_1 = {1, 2, "zs", 17}
# print(type(set_1))
# print(set_1)

# 2)
# set_2 = set("hello")
# print(set_2)

# 添加
# set_1 = {1, 2, 3}
# # set_1.add(4)
# # set_1.update("4","5")
# tup_1={6,7,8}
# set_1.update(tup_1)
# print(set_1)

# 移除
set_1={1,2,3}
set_1.remove(3)
print(set_1)



