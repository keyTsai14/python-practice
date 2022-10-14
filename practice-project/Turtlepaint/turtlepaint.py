"""
Turtle模块提供了在二维平面上移动的环境。
Turtle可以实现位置、航向和各种可能的状态和动作。
"""
import turtle as tu

roo = tu.Turtle() # 创建对象
wn = tu.Screen() # 屏幕对象
wn.bgcolor("black") # 屏幕背景
wn.title("标题")
roo.left(90) # 移动
roo.speed(20) # 速度

def draw(l,color): # 以长度‘l’作为参数的递归函数
    if l < 10:
        return
    else:
        roo.pensize(2)
        roo.pencolor(color)
        roo.forward(l)
        roo.left(30)
        draw(3*l/4,color)
        roo.right(60)
        draw(3*l/4,color)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

def draw1(l,color): # 以长度‘l’作为参数的递归函数
    if l < 10:
        return
    else:
        roo.pensize(3)
        roo.pencolor(color)
        roo.forward(l)
        roo.left(30)
        draw1(4*l/5,color)
        roo.right(60)
        draw1(4*l/5,color)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)

def draw2(l,color): # 以长度‘l’作为参数的递归函数
    if l < 10:
        return
    else:
        roo.pensize(2)
        roo.pencolor(color)
        roo.forward(l)
        roo.left(30)
        draw2(6*l/7,color)
        roo.right(60)
        draw2(6*l/7,color)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)  

colors = ["magenta","red",'#FFF8DC',"lightgreen","cyan"]
colors1 = ["magenta","red",'#FFF8DC',"lightgreen","cyan"]
colors2 = ["magenta","red",'#FFF8DC',"lightgreen","cyan"]

draw(20,"black")
roo.right(90)
roo.speed(2000)

def direction(i):
    if i % 2 == 0:
        roo.left(270)
        roo.speed(2000)
    else:
        roo.right(90)
        roo.speed(2000)


def startprint():
    i = 1
    for color in colors:
        draw(20,color)
        direction(i)
        i+=1
    i = 1
    for color in colors1:
        draw1(40,color)
        direction(i)
        i+=1
    i = 1
    for color in colors2:
        draw2(60,color)
        direction(i)
        i+=1      

    wn.exitonclick()

if __name__ == "__main__":
    startprint()
