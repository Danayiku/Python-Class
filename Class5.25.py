from turtle import *
speed(0)
color ('pink')
begin_fill()
number = 0
# while condition loops, run from 0 to 8
while number < 8:
    if number  < 4:
        forward(10)
        left(90)
        forward(10)
        left(90)
        forward(10)
        left(90)
        forward (30)
        left (90)
        forward (30)
        left (90)
        forward (30)
        left (90)
        forward (30)
        left (90)
        forward (30)
        left (90)
        forward (60)
        left (90)
        forward (60)
        left (90)
        forward (60)
        left (90)
        forward (60)
        left (90)
    if number >= 4:
        forward (100)
        left (90)
        forward (100)
        left (90)
        forward (100)
        left (90)
    number = number + 1 # number += 1
end_fill()
done()