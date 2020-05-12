# 实现简单计算器的图形界面
import tkinter as tk

win = tk.Tk()
win.title("整数计算器")  # 标题
win.geometry("240x264")  # 宽x高
win.resizable(False, False)  # 设置宽、高是否可以改变

# 文本输入框
result = tk.StringVar()
result.set("0")
ent = tk.Entry(win, textvariable=result)
ent.place(x=0, y=0, width=240, height=24)

# 创建键盘区
btn_list = ["1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "C", "0", "=", "/"]

# 添加功能
opt = 0  # 获取输入的数字
ope = ""  # 保存操作符
save = 0  # 保存前一个运算数字


def calc(event):
    """计算机的加减乘除功能"""
    global opt
    global ope
    global save
    # 点击数字键盘1-9
    if event.widget["text"] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # 获取被点击按钮的文本
        opt = opt * 10 + int(event.widget["text"])
        result.set(str(opt))
    # 点击加、减、乘、除
    elif event.widget["text"] in ["+", "-", "*", "/"]:
        save = opt
        ope = event.widget["text"]
        opt = 0
        result.set("0")
    # 点击C清空按钮
    elif event.widget["text"] == "C":
        opt = 0
        result.set("0")
    # 点击等于号
    elif event.widget["text"] == "=":
        if ope == "+":
            result.set(str(save + opt))
        if ope == "-":
            result.set(str(save - opt))
        if ope == "*":
            result.set(str(save * opt))
        if ope == "/":
            result.set(str(save / opt))


for i in range(16):
    strBtn = tk.StringVar()
    strBtn.set(btn_list[i])
    btn = tk.Button(win, textvariable=strBtn)
    btn.place(x=i % 4 * 60, y=i // 4 * 60 + 24, width=60, height=60)
    btn.bind("<Button-1>", calc)
tk.mainloop()
