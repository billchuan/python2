import hk_project1.resident_tools

while True:
    hk_project1.resident_tools.show_menu()
    action_str = input("请选择需要执行的操作:")
    print("你选择的是【%s】" % action_str)
    if action_str in ["1", "2", "3", "4"]:
        # 新增居民
        if action_str == "1":
            hk_project1.resident_tools.new_resident()
        # 显示全部
        if action_str == "2":
            hk_project1.resident_tools.show_all()
        # 搜索居民
        if action_str == "3":
            hk_project1.resident_tools.search_resident()
        elif action_str == "4":
            print("欢迎再次使用【居民管理系统】")
            break
    else:
        print("你输入的不正确，请重新选择")
