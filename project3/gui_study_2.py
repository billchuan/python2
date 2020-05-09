# 5月9日七、八节课学习























# 习题一
# import tkinter as tk
#
# top = tk.Tk()
# top.title("我的窗口")
# top.geometry("200x300")
# top.resizable(False, False)
#
# entry1 = tk.Entry(top)
# entry1.pack()
#
#
# def pr(event):
#     print(entry1.get())
#
#
# btn = tk.Button(top, text="打印")
# btn.bind("<Button-1>", pr)
# btn.pack()
# top.mainloop()

# 习题二
# import tkinter
# import tkinter as tk
#
# top = tk.Tk()
# top.title("我的窗口")
# top.geometry("300x200")
# top.resizable(False, False)
#
# list = tk.Listbox(top)
# for person_info in ["姓名：白嫖的勇士", "年龄：20", "电话：123123132123"]:
#     list.insert(tkinter.END, person_info)
# list.pack()
# top.mainloop()
