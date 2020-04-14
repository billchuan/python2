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
    sex_str = input("请输入性别:")
    age_str = input("请输入年龄:")
    tel_str= input("请输入电话:")
    addr_str=input("请输入地址:")
    resident_dict = {
        "姓名:": name_str,
        "性别:": sex_str,
        "年龄:": age_str,
        "电话:":tel_str,
        "地址:":addr_str
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
    for title in ["姓名", "性别", "年龄","电话","地址"]:
        print(title, end="\t\t")
    print("")
    print("*" * 41)
    for resident_dict in resident_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t" %
              (resident_dict["姓名:"],
               resident_dict["性别:"],
               resident_dict["年龄:"],
               resident_dict["电话:"],
               resident_dict["地址:"]))
    print("*" * 41)


def search_resident():
    """搜索居民"""
    print("*" * 41)
    find_name = input("请输入要搜索的居民姓名:")
    print("*" * 41)
    for resident_dict in resident_list:
        if resident_dict["姓名:"] == find_name:
            print("找到了%s的信息,具体如下" % find_name)
            print("*"*41)
            print("姓名\t\t性别\t\t年龄\t\t电话\t\t地址")
            print("-"*41)
            print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t" %
                  (resident_dict["姓名:"],
                   resident_dict["性别:"],
                   resident_dict["年龄:"],
                   resident_dict["电话:"],
                   resident_dict["地址:"]))
            print("*" * 41)
            break
        else:
           print("抱歉，没有找到%s的任何信息" % find_name)
           print("*"*41)
           break
