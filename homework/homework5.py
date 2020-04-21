# 4月21日作业
# file_1 = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt", encoding="UTF-8")
# while True:
#     text_1 = file_1.readline()
#     if len(text_1) == 0:
#         break
#     print(text_1, end=" ")
# file_1.close()

file_2 = open("C:\\Users\\Lenovo\\Desktop\\myinfo.txt","w+",encoding="UTF-8")
text_2 = file_2.write("i come from guizhou province")
file_2.close()
