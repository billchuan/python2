import tkinter as tk

win = tk.Tk()
win.title("整数计算器")
win.geometry("240x264")  # 宽x高
win.resizable(False, False)
# 文本输入框
result = tk.StringVar()
ent = tk.Entry(win, textvariable=result)
ent.place(x=0, y=0, width=240, height=24)
result.set("0")

# 创建键盘区
txts = ["1", "2", "3", "+",
        "4", "5", "6", "-",
        "7", "8", "9", "*",
        "C", "0", "=", "/"]

for i in range(16):
    strBtn = tk.StringVar()
    strBtn.set(txts[i])
    btn = tk.Button(win, textvariable=strBtn)
    btn.place(x=i % 4 * 60, y=i // 4 * 60 + 24, width=60, height=60)

tk.mainloop()
