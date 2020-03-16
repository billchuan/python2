import turtle
import time

turtle.pensize(5)
turtle.penjor("yellow") #画笔黄色
turtle.filljor("red") #内部填充红色


turtle.begin_fill()
for _ in range(5): #重复执行5次
    turtle.forward(200) #向前移动200步
    turtle.right(144)  #向右移动144
turtle.end_fill() #结束填充红色
time.sleep(1)

turtle.penup() #pen移动时不绘制图形
turtle.goto(-150,-120) #走到某个坐标位置

turtle.mainloop()
