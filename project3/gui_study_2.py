# 5月9日七、八节课学习
# 位置坐标网格
# import tkinter as tk
#
# top = tk.Tk()
# top.title("我的窗口")
# top.geometry("300x500")
# top.resizable(True, True)  # 宽、高是否能改变
#
# # 第1个按钮
# text_str = tk.StringVar()
# text_str.set("按钮1")
# btn1 = tk.Button(top, textvariable=text_str)
# btn1.place(x=50, y=50, width=50, height=100)
# top.mainloop()

# label组件
import tkinter as tk

top = tk.Tk()
top.title("我的窗口")
top.geometry("300x200")
top.resizable(False, False)

# 创建标签组件
label_bar = tk.StringVar()
label_bar.set("请输入你的姓名：")
label_obj = tk.Label(top, textvariable=label_bar)
label_obj.pack()
top.mainloop()

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
