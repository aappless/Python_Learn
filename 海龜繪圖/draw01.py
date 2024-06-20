import turtle
# 設置畫面
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -200)
t.pendown()

# 畫一朵花
def draw_flower(size):
    for i in range(10):
        t.forward(size)
        t.left(36)
        for j in range(5):
            t.forward(size/4)
            t.left(72)
        t.forward(size)
        t.left(36)

# 畫出花朵
draw_flower(50)

# 保持畫面
turtle.done()