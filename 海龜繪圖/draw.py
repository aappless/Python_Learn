# 這繪圖沒啥用 只是一個 GAME 吧
import turtle
# 指令
# forward()
# backward()
# left()
# right()
# circle()
# color()
# pensize()
# begin_fill()
# end_fill()

turtle.showturtle()
turtle.write('哈囉')
turtle.forward(300)
turtle.color('red')
turtle.left(90)

for i in range(0,13):
    turtle.penup() #收起画笔
    turtle.goto(0,0) #移到原点，移到会带有轨迹（画笔已经收起，所以没有轨迹）
    turtle.pendown() #放下笔开始画
    turtle.width(10)
    turtle.color("grey")
    turtle.forward(200)
    turtle.begin_fill()
    turtle.color("pink")
    turtle.fillcolor("pink")
    turtle.circle(55,240) # 55为圆的半径  240为画圆的三分之二
    turtle.forward(60-3*i)
    turtle.end_fill()
    turtle.right(18)            
turtle.mainloop() #停止画笔绘制   
