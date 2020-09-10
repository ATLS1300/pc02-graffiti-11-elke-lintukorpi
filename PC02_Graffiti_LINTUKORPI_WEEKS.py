#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:43:41 2020

@author: elkelintukorpi
"""

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
Turtle()

up()
#hair start
speed(10)
left(90)
forward(230)
dot(40)
left(90)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(15)
forward(20)
dot(40)
left(90)
forward(20)
dot(50)
left(90)
forward(30)
dot(50)
right(30)
forward(30)
dot(50)
right(20)
forward(30)
dot(50)
right(40)
forward(40)
dot(40)
right(30)
forward(20)
dot(30)
#hair done
color('DeepPink1')
left(200)
forward(70)
down()
begin_poly()
forward(30)
left(90)
forward(10)
left(90)
forward(30)
left(90)
forward(10)
end_poly()
#hair clip done
up()
goto(70,-45)
width(50)
color(200,180,0)
down()
forward(200)
up()
goto(40,-180)
down()
backward(70)
up()
goto(60,180)
color('DarkOrange1','brown2')
begin_fill()
for i in range(6):
  forward(100)
  right(60)
end_fill()

goto(-200,50)
width(10)
color('CadetBlue1')
down()
circle(30)

done()



 









