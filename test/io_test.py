# Python磁盘读写


if __name__ == "__main__":
    from sys import stdout

    filename = input("请输入文件名:\n")
    fp = open(filename, "w")
    ch = input("请输入字符串:\n")
    while ch != "#":
        fp.write(ch)
        fp.write("\n")
        stdout.write(ch)
        ch =input(" ")
    fp.close()
