import tkinter as tk

win = tk.Tk()
win.title("王海川的窗口")  # 标题
win.geometry("240x264")  # 宽x高
win.resizable(False, False)  # 设置宽、高是否可以改变

# 添加组件
label_1 = tk.Label(win, text="请输入姓名1：")
entry_1 = tk.Entry(win)
label_2 = tk.Label(win, text="请输入姓名2：")
entry_2 = tk.Entry(win)
# 设置组件位置以及组件大小
label_1.place(x=0, y=0, width=100, height=20)
entry_1.place(x=100, y=0, width=100, height=20)
label_2.place(x=0, y=20, width=100, height=20)
entry_2.place(x=100, y=20, width=100, height=20)


# 定义按钮事件
def btn_clicked(event):
    entry_2.delete(0, tk.END)  # 删除第二个文本框中的内容
    text = entry_1.get()  # 获取第一个文本框中的内容
    entry_2.insert(0, text)  # 设置第二个文本框中的内容


# 设置按钮
btn = tk.Button(win, text="文本复制")
btn.bind("<Button-1>", btn_clicked)  # 绑定按钮事件
btn.place(x=0, y=40, width=100, height=20)

tk.mainloop()
