# 4月21日五、六节学习
# 习题1
# file = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt",encoding="UTF-8",errors="ignore")
# while True:
#     text=file.readline()
#     if len(text)==0:
#         break
#     print(text,end=" ")
# file.close()

# 习题2
# file = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt", "a", encoding="UTF-8", errors="ignore")
# try:
#     file.write(" i am chinese")
#     print("写入成功")
# except Exception as result:
#     print("写入失败%s" % result)
# file.close()

# 文件的读取

# 打开文件
# file_1 = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt", encoding="UTF-8")
# # 读取文件
# text_1 = file_1.read()
# # 打印内容
# print(text_1)
# # 关闭文件
# file_1.close()

# 往文件中写数据
# 打开文件
# file_obj=open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt","a", encoding="UTF-8")
# # 写入数据
# file_obj.write("lisi")
# # 关闭文件
# file_obj.close()

# 文件的复制
# 打开文件
file1 = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt", "r", encoding="UTF-8")
file2 = open("C:\\Users\\Lenovo\\Desktop\\myinfo2.txt", "w", encoding="UTF-8")
# 读取和写入
# 读取文件1中数据
text_1 = file1.read()
# 写入文件2
file2.write(text_1)
# 关闭文件
file1.close()
file2.close()
