# 记录所有居民字典
resident_list = []


def show_menu():
    """显示菜单"""
    menu_info = """****欢迎使用【居民管理系统】V1.0****
*          1.新增居民            *
*          2.显示全部            *
*          3.搜索居民            *
*          4.退出系统            *
*********************************"""
    print(menu_info)


def new_resident():
    """新增居民"""
    print("*" * 33)
    name_str = input("请输入姓名:")
    add_str = input("请输入小区名:")
    stais_num_str = input("请输入楼梯号:")
    room_num_str = input("请输入房间号:")
    resident_dict = {
        "姓名:": name_str,
        "小区名:": add_str,
        "楼梯号:": stais_num_str,
        "房间号:": room_num_str,
    }
    resident_list.append(resident_dict)
    print("*" * 33)
    print("*     添加姓名为%s的居民成功      *" % name_str)
    print("*" * 33)


def show_all():
    """显示所有居民"""
    print("*" * 41)

    if len(resident_list) == 0:
        print("当前没有任何居民的信息")
        return
    for title in ["姓名", "小区名", "楼梯号", "房间号"]:
        print(title, end="\t\t")
    print("")
    print("*" * 41)
    for resident_dict in resident_list:
        print("%s\t\t%s\t\t%s\t\t%s\t" %
              (resident_dict["姓名:"],
               resident_dict["小区名:"],
               resident_dict["楼梯号:"],
               resident_dict["房间号:"]))
    print("*" * 41)


def search_resident():
    """搜索居民"""
    print("*" * 41)
    find_name = input("请输入要搜索的居民姓名:")
    print("*" * 41)
    for resident_dict in resident_list:
        if resident_dict["姓名:"] == find_name:
            print("找到了%s的信息,具体如下" % find_name)
            print("*" * 41)
            print("姓名\t\t小区名\t\t楼梯号\t\t房间号")
            print("-" * 41)
            print("%s\t\t%s\t\t%s\t\t%s\t" %
                  (resident_dict["姓名:"],
                   resident_dict["小区名:"],
                   resident_dict["楼梯号:"],
                   resident_dict["房间号:"]))
            print("*" * 41)
            break
        else:
            print("抱歉，没有找到%s的任何信息" % find_name)
            print("*" * 41)
            break
