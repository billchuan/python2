# 函数递归作业


def print_num(num):
    if num == 4:
        print("达到最里层文件夹，找到机密文件。开始返回")
        return
    print("进入第%d层文件夹" % num)
    print_num(num + 1)
    print("从第%d层文件夹返回" % num)


print_num(1)
