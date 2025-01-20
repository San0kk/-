from turtle import *

m = 2
fillcolor("red")
begin_fill()
for i in range(37):
    forward(10*m)
    right(10)
end_fill()
fillcolor("green")
begin_fill()
left(90)
forward(15)
right(35)
for i in range(12):
    right(3)
    forward(7)
right(120)
for i in range(13):
    forward(7)
    right(7)
right(10)
end_fill()
fillcolor("green")
begin_fill()
for i in range(12):
    left(3)
    forward(7)
left(120)
for i in range(13):
    forward(7)
    left(7)
end_fill()

done()