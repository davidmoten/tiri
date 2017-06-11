Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> ti=turtle.
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> ti = turtle.Pen()
>>> ti.shape
<bound method Turtle.shape of <turtle.Turtle object at 0x7f2a1694c048>>
>>> 
KeyboardInterrupt
>>> ti.shape("turtle")
>>> ti.turtlesize(2)
>>> ti.color(violet)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ti.color(violet)
NameError: name 'violet' is not defined
>>> ti.color ("violet")
>>> ti.up()
>>> ti.back(150)
>>> ti.forward(150)
>>> ti.down(100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ti.down(100)
TypeError: pendown() takes 1 positional argument but 2 were given
>>> ti.circle(100)
>>> ti.down()
>>> ti.circle(100)
>>> ti.restart()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    ti.restart()
AttributeError: 'Turtle' object has no attribute 'restart'
>>> import turtle
>>> ti=turtle.Pen()
>>> ti.shape("turtle")
>>> ti.turtlesize(2)
>>> ti.color("violet")
>>> ti.circle(30)
>>> ti.circle(-50)
>>> ti.color("yellow")
>>> ti.circle(80)
>>> ti.circle(-90)
>>> ti.color("cyan")
>>> ti.up()
>>> ti.forward(150)
>>> ti.forward(150)
>>> ti.circle(30)
>>> ti.down()
>>> ti.forward(150)
>>> ti.back(150)
>>> ti.circle(30)
>>> ti.color("orange")
>>> ti.circle(40)
>>> ti.color("yellow")
>>> ti.circle(50)
>>> ti.color("lavender")
>>> ti.circle(60)
>>> ti.left(45)
>>> ti.left(45)
>>> ti.color("deepskyblue")
>>> ti.forward(50)
>>> ti.circle(20)
>>> ti.color("mediumspringgreen")
>>> ti.right(45)
>>> ti.forward(150)
>>> ti.circle(50)
>>> ti.up()
>>> ti.forward(10)
>>> ti.circle(50)
>>> ti.forward(20)
>>> ti.circle(50)
>>> ti.down()
>>> ti.circle(50)
>>> ti.back(15)
>>> ti.color("")
